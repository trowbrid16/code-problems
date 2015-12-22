def balanced_brackets(string):
	#dictionary for matching brackets
	brackets = {"(":")", "[":"]", "{":"}"}

	#can't have matches in odd length string
	if len(string) % 2 == 1:
		return False

	stack = []
	#iterate through list and match brackets
	for i in range(len(string)):
		currChar = string[i]
		if currChar in brackets.keys():
			#open bracket, push val to stack
			stack.append(brackets[string[i]])

		elif currChar in brackets.values():
			#closed bracket, check top of stack
			if stack[-1] == currChar:
				stack.pop()
				
		else:
			#not a bracket character, ignore
			pass

	#true iff stack is empty
	return not stack

#prompt for user input
print balanced_brackets(raw_input("Please enter a string: "))