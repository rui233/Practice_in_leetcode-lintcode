class Solution:
	def lengthOfLastWord(selfself,s):
		'''

		:type s:str
		:rtupe:int
		'''

		count = 0
		local_count = 0

		for i in range(len(s)):
			if s[i] == ' ':
				local_count = 0
			else :
				local_count += 1
				count = local_count
			return count