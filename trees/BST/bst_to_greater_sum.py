'''
1038. Binary Search Tree to Greater Sum Tree

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree
such that every key of the original BST is changed to the original key plus
sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these constraints:
The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Note: This question is the same as 538: https://leetcode.com/problems/convert-bst-to-greater-tree/

Examples:
Input: root = [4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]
Output: [30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]

Input: root = [0,null,1]
Output: [1,null,1]

Input: root = [1,0,2]
Output: [3,3,2]

Input: root = [3,2,4,1]
Output: [7,9,4,10]
'''


class Solution(object):
    def bstToGst(self, root):

        self.sum = 0

        def reverseInorder(self, root):
            if not root:
                return

            reverseInorder(self, root.right)
            root.val += self.sum  # change the current node with sum of all previos node values
            self.sum = root.val  # update the root_sum for the next node
            reverseInorder(self, root.left)

        reverseInorder(self, root)
        return root
