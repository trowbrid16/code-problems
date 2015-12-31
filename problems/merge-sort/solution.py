from collections import deque
import random

def merge(list1, list2):
	mergedList = []

	# setup lists for queue operations
	list1 = deque(list1)
	list2 = deque(list2)

	while list1 and list2:
		# repeat until one list is empty
		if list1[0] < list2[0]:
			mergedList.append(list1.popleft())
		else:
			mergedList.append(list2.popleft())

	# append the non-empty list to the mergedList
	if not list1:
		[mergedList.append(x) for x in list(list2)]
	else:
		[mergedList.append(x) for x in list(list1)]

	return mergedList

def mergeSort(list1):
	if len(list1) == 0 or len(list1) == 1:
		return list1

	#find the mid point
	split = len(list1)/2

	return merge(mergeSort(list1[split:]), mergeSort(list1[:split]))

sortThis = [random.randint(0,1000) for x in range(20)]

print sortThis
print "====================="
print mergeSort(sortThis)