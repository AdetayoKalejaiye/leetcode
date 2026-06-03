from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
README_PATH = ROOT / "README.MD"
TOPICS_PATH = ROOT / "topics.json"
SECTION_START = "<!-- TOPICS:START -->"
SECTION_END = "<!-- TOPICS:END -->"


def load_topics() -> list[dict[str, object]]:
    data = json.loads(TOPICS_PATH.read_text(encoding="utf-8"))
    topics = data.get("topics", [])
    if not isinstance(topics, list):
        raise ValueError("topics.json must contain a 'topics' list")
    return topics


def list_solution_folders() -> list[str]:
    folders = []
    for entry in ROOT.iterdir():
        if not entry.is_dir():
            continue
        if entry.name in {".git", ".github"}:
            continue
        folders.append(entry.name)
    return sorted(folders)


def build_section(topics: list[dict[str, object]], folders: list[str]) -> str:
    lines: list[str] = []
    used: set[str] = set()

    for topic in topics:
        name = topic.get("name")
        entries = topic.get("folders")
        if not isinstance(name, str) or not isinstance(entries, list):
            raise ValueError("Each topic must include 'name' and 'folders'")

        topic_folders = [folder for folder in entries if folder in folders]
        if not topic_folders:
            continue

        lines.append(f"### {name}")
        for folder in topic_folders:
            lines.append(f"- [{folder}](./{folder})")
        lines.append("")
        used.update(topic_folders)

    remaining = [folder for folder in folders if folder not in used]
    if remaining:
        lines.append("### Uncategorized")
        for folder in remaining:
            lines.append(f"- [{folder}](./{folder})")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


def update_readme(section: str) -> None:
    content = README_PATH.read_text(encoding="utf-8")
    if SECTION_START in content and SECTION_END in content:
        before, remainder = content.split(SECTION_START, 1)
        _, after = remainder.split(SECTION_END, 1)
        updated = f"{before}{SECTION_START}\n{section}{SECTION_END}{after}"
    else:
        header = "## Topics\n\n" if "## Topics" not in content else ""
        updated = (
            content.rstrip()
            + "\n\n"
            + header
            + SECTION_START
            + "\n"
            + section
            + SECTION_END
            + "\n"
        )

    if updated != content:
        README_PATH.write_text(updated, encoding="utf-8")


def main() -> None:
    topics = load_topics()
    folders = list_solution_folders()
    section = build_section(topics, folders)
    update_readme(section)


if __name__ == "__main__":
    main()
