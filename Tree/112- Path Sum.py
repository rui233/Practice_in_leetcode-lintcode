class Solution(object):
	def hasPathSum(self,root,sum):
		"""

		:type root: TreeNode
		:type sum: int
		:rtype: bool
		"""
	if root is None:
		return False
	if root.left is None and root.right is None and root.val == sum:
		return True
	else:
		return self.hasPathSum(root.left, sum = root.val)
