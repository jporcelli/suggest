"""
__author__ James Porcelli

Prefix tree 
"""

"""
A node in the tree
"""
class Node:

	def __init__(self, char, level, value=None):
		self.children = {}
		self.char = char
		self.child_count = 0
		self.level = level

		if value is not None:
			self.value = value

	def add_child(self, node):
		self.child_count = self.child_count + 1
		self.children[node.char] = node

	def get_child(self, char):
		if char in self.children:
			return self.children[char]
		else:
			return None

	def __str__(self):
		return self.char
		
	def __repr__(self):
		return self.__str__()

"""
Classic pre-fix tree, or Trie.
"""
class Trie:
	def __init__(self):
		#root node corresponds to empty string
		self.root = Node('', 0)

	"""
	Insert a new word into the tree.

	string - The word to insert
	"""
	def insert(self, string, value=None):
		i = 0
		n = len(string)
		node = self.root

		while i < n:
			if string[i] in node.children:
				node = node.get_child(string[i])
				i = i + 1
			else:
				break

		#append new nodes, if necessary
		while i < n:
			node.add_child(Node(string[i], i + 1) )
			node = node.get_child(string[i])
			i = i + 1

		#add a value to the new word if desired
		if value is not None:
			node.value = value


	"""
	Modified pre-order search to collect the paths
	in the tree which have the specified node as an 
	ancestor.

	node - The node from which we start the search. Represents
		the prefix under consideration.
	"""
	def pre_order(self, node, prefix):
		s= []
		words= []
		s.append(node)
		word = prefix[:len(prefix) - 1]
		prev_wrd_lvl = 0
		flag = False

		if node is None:
			return []

		while len(s) > 0:
			v = s.pop()

			if flag:
				k = prev_wrd_lvl - v.level
				word = word[:len(word) - (k + 1)] + v.char
				flag = False
			else:
				word = word + v.char

			if v.child_count == 0:
					words.append(word)
					prev_wrd_lvl = v.level
					flag = True				
			else:
				for i in v.children:
					s.append(v.get_child(i))

		return words


	"""
	Returns a tuple of values corresponding to paths
	in the tree orignating from the specified prefix,
	i.e descendants of the prefix

	n - The number of descendants to return
	prefix - The prefix to search on
	"""
	def getDescendents(self, prefix):
		i = 0
		n = len(prefix)
		node = self.root

		while i < n:
			if prefix[i] in node.children:
				node = node.children[prefix[i]]
				i = i + 1
			else:
				return None

		return self.pre_order(node, prefix)


#DEV ONLY
if __name__ == '__main__':
	#Test the Trie implementation
	t = Trie()

	with open('input.txt', 'rt') as f:
		for line in f:
			t.insert( line.strip('\n ') )

	print(t.getDescendents('par'))





