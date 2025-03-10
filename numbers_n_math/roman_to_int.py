'''
13. Roman to Integer
https://leetcode.com/problems/roman-to-integer/
Credit: https://www.youtube.com/watch?v=MUUc4GFvlL0

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two one's added together. 
12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Examples
Input: s = "III" -> 3
Input: s = "IV" -> 4
Input: s = "IX" -> 9
Input: s = "LVIII" -> 58
Explanation: L = 50, V= 5, III = 3.

Input: s = "MCMXCIV" -> 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''


def romanToInt(s: str) -> int:
    mapping = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    prev = curr = total = 0

    for roman in s:
        curr = mapping[roman]
        total += curr

        if curr > prev:
            total = total - (2 * prev)

        prev = curr

    return total


assert romanToInt("III") == 3
assert romanToInt("IV") == 4
assert romanToInt("IX") == 9
assert romanToInt("LVIII") == 58
assert romanToInt("MCMXCIV") == 1994
