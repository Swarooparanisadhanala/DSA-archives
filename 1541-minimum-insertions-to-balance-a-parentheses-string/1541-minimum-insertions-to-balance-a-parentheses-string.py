class Solution:

    def minInsertions(self, s: str) -> int:
        insertions = 0
        open_needed = 0  # Count of needed '('

        i = 0
        n = len(s)

        while i < n:
            if s[i] == "(":
                open_needed += 1
                i += 1
            else:
                # We encountered a ')'
                # Check if it's a double closing parenthesis '))'
                if i + 1 < n and s[i + 1] == ")":
                    i += 2
                else:
                    # Single ')', so we need 1 additional ')' to make it '))'
                    insertions += 1
                    i += 1

                # Match with an open bracket '('
                if open_needed > 0:
                    open_needed -= 1
                else:
                    # Missing an open bracket '(' before this '))'
                    insertions += 1

        # Each unmatched '(' requires '))' (2 insertions)
        insertions += open_needed * 2

        return insertions