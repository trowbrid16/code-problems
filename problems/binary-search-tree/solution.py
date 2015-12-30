import random
class Tree:
	def __init__(self):
		self.root = None

	def insertValue(self, value):
		if self.root == None:
			self.root = TreeNode(value)
		else:
			self._insertValue(value, self.root)

	def _insertValue(self, value, root):
		newNode = TreeNode(value)

		if value == root.value:
			# do not insert
			print "Value: " + `value` + " already exists."

		elif value > root.value:
			# insert to the right
			if root.right == None:
				root.right = newNode
			else:
				self._insertValue(value, root.right)

		else:
			#insert to the left
			if root.left == None:
				root.left = newNode
			else:
				self._insertValue(value, root.left)

	def deleteValue(self, value):
		self._deleteValue(value, self.root, None)

	def _deleteValue(self, value, root, parent):
		if root == None:
			print `value` + " does not exist"
			return False

		elif value > root.value:
			return self._deleteValue(value, root.right, root)

		elif value < root.value:
			return self._deleteValue(value, root.left, root)

		elif root.value == value:
			if root.left == None and root.right == None:
				# no children
				# simply remove the node
				if parent.value > root.value:
					parent.left = None
				else:
					parent.right = None

				root = None
				return True

			elif root.left == None and root.right != None:
				# child to the right
				# check parentage
				if parent.value > root.value:
					# root is parents left child
					parent.left = root.right
				else:
					# root is parents right child
					parent.right = root.right

				root = None
				return True

			elif root.left != None and root.right == None:
				# child to the left
				# check parentage
				if parent.value > root.value:
					# root is parents left child
					parent.left = root.left
				else:
					# root is parents right child
					parent.right = root.left

				root = None
				return True

			else:
				# two children
				successorVal = self.findMax(root.left).value

				root.value = successorVal

				return self._deleteValue(successorVal, root.left, root)


	def findMax(self, root):
		if root.right == None:
			return root

		return self.findMax(root.right)

	def printTree(self):
		self._printTree(self.root)

	def _printTree(self, root):
		if root == None:
			return

		self._printTree(root.left)
		print root.value		
		self._printTree(root.right)

class TreeNode:	
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None


#unit testing
tree = Tree()
toInsert = [1,2,3,4,5,6,7,8,9,10]
toDelete = [3,7,2]

#insert some values
for i in toInsert:
	tree.insertValue(i)

tree.printTree()
print "================="
for i in toDelete:
	if tree.deleteValue(i):
		deleted.append(i)
	
print "Deleted values: " + `toDelete`
tree.printTree()