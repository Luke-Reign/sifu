"""
Count of index pairs with equal elements in an array
Given an array of n elements.
The task is to count the total number of indices (i, j) such that arr[i] = arr[j] and i != j

Examples :
Input : arr[] = {1, 1, 2}: -> 1
As arr[0] = arr[1], the pair of indices is (0, 1)

Input : arr[] = {1, 1, 1} -> 3
As arr[0] = arr[1], the pair of indices is (0, 1), 
(0, 2) and (1, 2)

Input : arr[] = {1, 2, 3} -> 0
"""


def countPairs(arr):
    n = len(arr)
    mapping = {}
    ans = 0

    # Finding frequency of each number.
    for num in arr:
        mapping[num] = mapping.get(num, 0) + 1

    # Calculating pairs of each value.
    for k, v in mapping.items():
        ans += (v * (v - 1)) // 2
    return ans


def countPairs3(arr):
    def no_of_repeats(n):
        if n < 2:
            return 0
        return n-1 + no_of_repeats(n-1)

    freqs = [arr.count(i) for i in list(set(arr))]
    res = sum([no_of_repeats(i) for i in freqs])
    return res


arr = [1, 1, 2]
arr1 = [1, 1, 1, 3, 3, 4, 1]
# print(countPairs(arr))
print(countPairs(arr1))
print(countPairs3(arr1))
