"""
Given a n-ary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

For example, given a 3-ary tree:



# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        if not root:
            return 0
        
        return self.traverse(root, 1);
        
    
    def traverse(self, node, count):
        if not node or not node.children:
            return count 
        
        return max(self.traverse(child, count + 1) for child in node.children)