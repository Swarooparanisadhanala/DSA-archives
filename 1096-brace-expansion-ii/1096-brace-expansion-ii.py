class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Operator stack and operand (set of strings) stack
        # Priorities / operations:
        # ',' represents set Union (lower precedence)
        # Concatenation represents Cartesian product (higher precedence)
        
        stack = []
        # Current group contains sub-expressions separated by commas: set union
        curr_union = set()
        # Current concatenation term within the comma section: set product
        curr_prod = {""}

        i = 0
        n = len(expression)

        while i < n:
            char = expression[i]

            if char == '{':
                # Push the current state to stack and reset state for new group
                stack.append(curr_union)
                stack.append(curr_prod)
                curr_union = set()
                curr_prod = {""}
                i += 1

            elif char == '}':
                # Finish the union within the current brace group
                curr_group_res = curr_union | curr_prod
                
                # Pop state prior to matching '{'
                prev_prod = stack.pop()
                prev_union = stack.pop()

                # Concatenate previous product with current group result
                curr_prod = {a + b for a in prev_prod for b in curr_group_res}
                curr_union = prev_union
                i += 1

            elif char == ',':
                # Finish current product term and add it to the union
                curr_union |= curr_prod
                curr_prod = {""}
                i += 1

            else:
                # Lowercase letter: parse full word
                j = i
                while j < n and expression[j].isalpha():
                    j += 1
                word = expression[i:j]
                
                # Concatenate with the current product
                curr_prod = {a + word for a in curr_prod}
                i = j

        # Combine final union and last product term
        res_set = curr_union | curr_prod
        return sorted(list(res_set))