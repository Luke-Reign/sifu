'''
34. Find First and Last Position of Element in Sorted Array
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
'''


def find_first_and_last(A, target):
    # Naive Approach -> O(n)
    n = len(A)
    first, last = -1, -1

    for i in range(n):
        if target != A[i]:
            continue

        if first != -1:
            continue
        else:
            first = i

        last = i

    return [first, last]


class Solution:
    def findFirstPosition(self, arr, target):
        start, end = 0, len(arr) - 1
        index = -1

        while (start <= end):
            mid = start + (end - start) / 2

            if arr[mid] == target:
                index = mid
                end = mid - 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return index

    def findLastPosition(self, arr, target):
        start, end = 0, len(arr) - 1
        index = -1

        while (start <= end):
            mid = start + (end - start) / 2

            if arr[mid] == target:
                index = mid
                end = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return index

    def searchRange(self, nums, target):
        first_index = self.findFirstPosition(arr, target)
        last_index = self.findLastPosition(arr, target)

        return [first_index, last_index]


soln = Solution()
arr = [1, 4, 7, 8, 11, 11, 11, 11, 11, 13]
target = 11
assert soln.searchRange(arr, target) == [4, 8]



'''
// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
// video tutorial: https://youtu.be/dVXy6hmE_0U
class Solution {
    int first_pos(vector<int>& a, int x) {
        int n = a.size();
        int first_pos = n; // first >= x
        int low = 0, high = n - 1;
        while(low <= high) {
            int mid = low + (high - low) / 2;
            if(a[mid] >= x) {
                first_pos = mid;
                high = mid - 1;
            }
            else { // a[mid] < x
                low = mid + 1;
            }
        }
        return first_pos;
    }
public:
    vector<int> searchRange(vector<int>& a, int x) {
        // lower_bound(a.begin(), a.end(), x);
        int first = first_pos(a, x);
        int last = first_pos(a, x + 1) - 1;
        if(first <= last) {
            return {first, last};
        }
        return {-1, -1};
    }
};
'''