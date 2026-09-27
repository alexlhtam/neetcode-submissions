class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {')': '(', '}': '{', ']': '['}
        seen = []

        for ch in s:
            if ch in bracket_map:
                top = seen.pop() if seen else '#'

                if bracket_map[ch] != top:
                    return False

            else:
                seen.append(ch)

        return len(seen) == 0