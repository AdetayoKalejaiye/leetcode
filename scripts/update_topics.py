#!/usr/bin/env python3
"""
Scans the repo root for solution folders/files, finds any that are NOT yet
listed in topics.json, asks a Groq-hosted model to slot each one into the
best-fitting EXISTING topic (only inventing a new topic when nothing fits),
writes the result back to topics.json, and regenerates the auto-generated
block in README.md.

No third-party dependencies — only the Python standard library, so the
GitHub Action doesn't need a `pip install` step.

Environment variables:
    GROQ_API_KEY              required, only used if there are new items
    GROQ_MODEL                 optional, defaults to llama-3.1-8b-instant
    GITHUB_REPOSITORY_OWNER   optional, used to build README links
    GITHUB_REPO_NAME           optional, used to build README links
    GITHUB_DEFAULT_BRANCH      optional, defaults to "main"
"""

import json
import os
import re
import sys
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TOPICS_JSON = REPO_ROOT / "topics.json"
README = REPO_ROOT / "README.md"

GITHUB_USER = os.environ.get("GITHUB_REPOSITORY_OWNER", "AdetayoKalejaiye")
REPO_NAME = os.environ.get("GITHUB_REPO_NAME", "leetcode")
BRANCH = os.environ.get("GITHUB_DEFAULT_BRANCH", "main")

# Groq's OpenAI-compatible chat completions endpoint.
GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"
# llama-3.1-8b-instant is Groq's cheapest/fastest model -- plenty for a
# short classification task. Override with GROQ_MODEL if you want something
# beefier (e.g. llama-3.3-70b-versatile) for trickier edge cases.
MODEL = os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant")

# Top-level entries that are not solutions and should never be classified.
IGNORE = {
    ".git", ".github", ".gitignore", ".gitattributes",
    "README.md", "topics.json", "scripts",
    "LICENSE", "LICENSE.md", ".vscode", "node_modules",
}

MARKER_START = "<!-- TOPICS:START -->"
MARKER_END = "<!-- TOPICS:END -->"

CODE_SUFFIXES = (".py", ".js", ".ts", ".java", ".cpp", ".c", ".go", ".rb", ".kt", ".swift")


def discover_items():
    """Top-level folder/file names in the repo that represent solutions."""
    items = []
    for entry in REPO_ROOT.iterdir():
        if entry.name in IGNORE or entry.name.startswith("."):
            continue
        items.append(entry.name)
    return sorted(items)


def load_topics():
    if TOPICS_JSON.exists():
        return json.loads(TOPICS_JSON.read_text())
    return {"topics": []}


def classified_set(data):
    s = set()
    for t in data["topics"]:
        s.update(t["folders"])
    return s


def read_snippet(name, max_chars=600):
    """Grab a short snippet of code to give the model real signal, not just a filename."""
    path = REPO_ROOT / name
    try:
        if path.is_file():
            return path.read_text(errors="ignore")[:max_chars]
        if path.is_dir():
            for child in sorted(path.iterdir()):
                if child.suffix in CODE_SUFFIXES:
                    return child.read_text(errors="ignore")[:max_chars]
    except Exception:
        pass
    return ""


def build_prompt(new_items, existing_topics):
    topics_block = "\n".join(f'- "{t["name"]}"' for t in existing_topics)

    item_blocks = []
    for name in new_items:
        snippet = read_snippet(name)
        if snippet:
            item_blocks.append(f"### {name}\n```\n{snippet}\n```")
        else:
            item_blocks.append(f"### {name}\n(no readable source found, classify by name alone)")
    items_block = "\n\n".join(item_blocks)

    return f"""You are maintaining the topic taxonomy for a LeetCode-style solutions repo.

Existing topic categories:
{topics_block}

Classify each item below into the SINGLE best-fitting EXISTING topic above.
Be decisive: prefer reusing an existing topic over inventing a new one.
Only propose a brand-new topic name if an item genuinely fits none of the
existing topics (e.g. a new algorithmic pattern not represented yet).
Never respond with "Uncategorized" or anything similar — always make a call.

Items to classify:
{items_block}

Respond with ONLY a JSON array and nothing else (no preamble, no markdown
fences), in exactly this shape:
[{{"item": "<name>", "topic": "<topic name, existing or new>"}}]
"""


def call_groq(prompt):
    api_key = os.environ["GROQ_API_KEY"]
    body = json.dumps({
        "model": MODEL,
        "temperature": 0,
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": prompt}],
    }).encode()
    req = urllib.request.Request(
        GROQ_URL,
        data=body,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        data = json.loads(resp.read().decode())

    text = data["choices"][0]["message"]["content"].strip()
    text = re.sub(r"^```(json)?\s*|\s*```$", "", text)
    return json.loads(text)


def apply_classifications(data, classifications):
    by_name = {t["name"]: t for t in data["topics"]}
    for c in classifications:
        item, topic_name = c["item"], c["topic"].strip()
        if topic_name not in by_name:
            new_topic = {"name": topic_name, "folders": []}
            data["topics"].append(new_topic)
            by_name[topic_name] = new_topic
        if item not in by_name[topic_name]["folders"]:
            by_name[topic_name]["folders"].append(item)
    return data


def render_topics_block(data, all_items):
    classified = classified_set(data)
    uncategorized = [i for i in all_items if i not in classified]

    lines = []
    for t in data["topics"]:
        if not t["folders"]:
            continue
        lines.append(f"### {t['name']}\n")
        for folder in sorted(t["folders"]):
            lines.append(
                f"* [{folder}](https://github.com/{GITHUB_USER}/{REPO_NAME}/blob/{BRANCH}/{folder})"
            )
        lines.append("")

    if uncategorized:
        lines.append("### Uncategorized\n")
        for folder in sorted(uncategorized):
            lines.append(
                f"* [{folder}](https://github.com/{GITHUB_USER}/{REPO_NAME}/blob/{BRANCH}/{folder})"
            )
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def update_readme(new_block):
    content = README.read_text() if README.exists() else "# README\n"

    if MARKER_START in content and MARKER_END in content:
        pattern = re.compile(re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END), re.DOTALL)
        content = pattern.sub(f"{MARKER_START}\n{new_block}{MARKER_END}", content)
    else:
        section = (
            "## Topics\n"
            "This section is auto-generated from `topics.json`. Do not edit by hand.\n\n"
            f"{MARKER_START}\n{new_block}{MARKER_END}\n"
        )
        heading = re.search(r"^##\s+Topics\b.*$", content, re.MULTILINE)
        if heading:
            rest = content[heading.end():]
            next_heading = re.search(r"\n##\s+\S", rest)
            end = heading.end() + (next_heading.start() if next_heading else len(rest))
            content = content[: heading.start()] + section + content[end:]
        else:
            content = content.rstrip() + "\n\n" + section

    README.write_text(content)


def main():
    data = load_topics()
    all_items = discover_items()
    already = classified_set(data)
    new_items = [i for i in all_items if i not in already]

    if new_items:
        if "GROQ_API_KEY" not in os.environ:
            print(f"New items found but GROQ_API_KEY is not set: {new_items}", file=sys.stderr)
            sys.exit(1)
        print(f"Classifying {len(new_items)} new item(s): {new_items}")
        prompt = build_prompt(new_items, data["topics"])
        classifications = call_groq(prompt)
        data = apply_classifications(data, classifications)
        TOPICS_JSON.write_text(json.dumps(data, indent=2) + "\n")
    else:
        print("No new items to classify.")

    update_readme(render_topics_block(data, all_items))


if __name__ == "__main__":
    main()
