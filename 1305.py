# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
   
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2

        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])

        return self.merge(left, right)


    def merge(self, left, right):
        result = []

        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Remaining elements
        result.extend(left[i:])
        result.extend(right[j:])

        return result
    def inorder(self, root : TreeNode, tree_list):
        if root:
            self.inorder(root.left, tree_list)
            tree_list.append(root.val)
            print(root.val)
            self.inorder(root.right, tree_list)
    def getAllElements(self, root1: TreeNode | None, root2: TreeNode | None) -> list[int]:
        tree1_list = []
        tree2_list = []
        self.inorder(root1, tree1_list)
        self.inorder(root2, tree2_list)
       
        return self.merge(tree1_list, tree2_list)


        
