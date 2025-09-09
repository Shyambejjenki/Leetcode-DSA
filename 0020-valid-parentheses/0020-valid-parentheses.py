class Solution:
    def isValid(self, s):
        stack = []
        mapping = {')': '(', ']': '[', '}': '{'}
        
        for char in s:
            if char in mapping:  # closing bracket
                top = stack.pop() if stack else '#'
                if mapping[char] != top:
                    return False
            else:  # opening bracket
                stack.append(char)
        
        return not stack


# ------------------------------
# Example Tests
# ------------------------------
solution = Solution()
print(solution.isValid("()"))      # True
print(solution.isValid("()[]{}"))  # True
print(solution.isValid("(]"))      # False
print(solution.isValid("([])"))    # True
print(solution.isValid("([)]"))    # False
