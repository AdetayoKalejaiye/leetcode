class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Extract non-underscore characters with their positions from start string
        # Each tuple contains (character, original_index)
        start_chars = [(char, index) for index, char in enumerate(start) if char != '_']
      
        # Extract non-underscore characters with their positions from target string
        target_chars = [(char, index) for index, char in enumerate(target) if char != '_']
      
        # If the number of non-underscore characters differs, transformation is impossible
        if len(start_chars) != len(target_chars):
            return False
      
        # Check each corresponding pair of characters
        for (start_char, start_pos), (target_char, target_pos) in zip(start_chars, target_chars):
            # Characters must match at corresponding positions (order preservation)
            if start_char != target_char:
                return False
          
            # 'L' can only move left, so its target position must be <= start position
            if start_char == 'L' and start_pos < target_pos:
                return False
          
            # 'R' can only move right, so its target position must be >= start position
            if start_char == 'R' and start_pos > target_pos:
                return False
      
        # All conditions satisfied, transformation is possible
        return True