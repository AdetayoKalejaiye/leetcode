from collections import Counter


class Solution:

    def findAnagrams(self, s: str, p: str) -> list[int]:
        left = 0
        result = []

        # Frequency map for the target pattern p
        p_count = Counter(p)

        # Initial right boundary of the window
        right = len(p) - 1

        # Frequency map for the initial window in s
        initial_window = s[left : right + 1]
        window_count = Counter(initial_window)

        # Slide the window across string s
        while right < len(s):

            # If frequencies match, record the start index of the anagram
            if window_count.items() == p_count.items():
                result.append(left)

            # Remove outgoing character from window frequency map
            outgoing_char = s[left]
            window_count[outgoing_char] -= 1
            if window_count[outgoing_char] == 0:
                del window_count[outgoing_char]

            # Shift the window right
            right += 1
            left += 1

            if right >= len(s):
                break

            # Add incoming character to window frequency map
            incoming_char = s[right]
            window_count[incoming_char] += 1

        return result
