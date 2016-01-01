from Tree import *
from collections import deque

def printTreeLevelOrder(tree):
	# setup for queue operations
	nodesOnLevel = [tree.root]
	treeHeight = tree.getHeight()
	lineWidth = 2**treeHeight
	# iteration counter
	level = 1

	while level <= treeHeight:
		# calculate the spacing before and after each node value
		preceding = "".join([" " for x in range(2**(treeHeight - level) - 1)])
		succeeding = "".join([" " for x in range(2**(treeHeight - level))])
		
		# create the line to be printed
		line = []
		for x in nodesOnLevel:
			# place spacers for null children
			if x.value == "_":
				line.append(preceding + x.value + succeeding)
			else:
				line.append(preceding + `x.value` + succeeding)
		
		# print the line
		print "".join(line)	

		# move to the next level in the tree
		newNodesOnLevel = []
		for i in nodesOnLevel:
			#check for null children
			if i.left != None:
				newNodesOnLevel.append(i.left)
			else:
				# assign filler value for null children
				newNodesOnLevel.append(TreeNode("_"))

			#check for null children
			if i.right != None:
				newNodesOnLevel.append(i.right)
			else:
				# assign filler value for null children
				newNodesOnLevel.append(TreeNode("_"))

		# update the nodesOnLevel
		nodesOnLevel = newNodesOnLevel
		level += 1

# Unit Testing
tree = Tree()
toInsert = [8,4,12,2,6,10,14,1,3,5,7,9,15]
toDelete = []

#insert some values
for i in toInsert:
	tree.insertValue(i)

print "Height " + `tree.getHeight()`
tree.printTree()
printTreeLevelOrder(tree)