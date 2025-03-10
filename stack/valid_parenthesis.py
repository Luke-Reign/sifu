"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Given a string containing just the characters
'(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Input: "()" -> Output: true
Input: "()[]{}" -> Output: true
Input: "(]" -> Output: false
Input: "([)]" -> Output: false
Input: "{[]}" -> Output: true
"""


def is_valid(_str: str) -> bool:
    stack = []
    matches = {'(': ')', '[': ']', '{': '}'}

    for char in _str:
        if char in matches:
            stack.append(char)
        else:
            if not stack:
                return False

            last_open_bracket = stack.pop()
            if matches[last_open_bracket] != char:
                return False

    return not stack


assert is_valid(']') is False
assert is_valid('()') is True
assert is_valid('()[]{}') is True
assert is_valid('(]') is False
assert is_valid('([)]') is False
assert is_valid('{[]}') is True
