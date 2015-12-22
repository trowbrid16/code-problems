index = int(raw_input("Please enter a position: "))

prev = 0
curr = 1
fibNumbers = [0,1]

while len(fibNumbers) < index + 1:
	fibNumbers.append(fibNumbers[curr] + fibNumbers[prev])

	curr += 1
	prev += 1

print fibNumbers[index]