class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        bracket_dict = {
            "]":"[",
            "}":"{",
            ")":"("
        }
        close_brackets = bracket_dict.keys()
        open_brackets = bracket_dict.values()
        bracket_stack = []
        for bracket in s:
            if bracket in open_brackets:
                bracket_stack.append(bracket)
                continue
            opening_bracket = bracket_dict[bracket]
            if not bracket_stack or opening_bracket != bracket_stack[-1]:
                return False
            bracket_stack.pop(-1)
        if bracket_stack:
            return False
        else:
            return True
            