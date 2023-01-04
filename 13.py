def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if valid(x,pivot) == 1:
                less.append(x)
            elif valid(x,pivot) == 0:
                equal.append(x)
            elif valid(x,pivot) == -1:
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


def valid(left, right):

	#print(left,right,len(left),len(right))

	if not len(left) and not len(right):
		return 0

	if not len(left):
		return 1

	if not len(right):
		return -1
	
	x = left[0]
	y = right[0]
	
	#print('\t',x,'  ',y)

	islist_left = isinstance(x, list)
	islist_right = isinstance(y, list)

	if not islist_left and not islist_right:
		if x > y:
			return -1
		if x < y:
			return 1
		
	elif islist_left and islist_right:
		is_valid = valid(x,y)

		if is_valid == -1:
			return -1
		if is_valid == 1:
			return 1
	else:
		if not islist_left:
			x = [x]
		else:
			y = [y]
		is_valid = valid(x,y)
		if is_valid == -1:
			return -1
		if is_valid == 1:
			return 1

	left = left[1:] if len(left) > 1 else []
	right = right[1:] if len(right) > 1 else []
	#left.pop(0)
	#right.pop(0)
	return valid(left,right)



def main():
	sol = 1
	index = 1
	packets = []
	while True:
		left = eval(input())
		right = eval(input())
		#print("INDEX    " + str(index)+'\n')
		'''
		if valid(left,right) == 1:
			#print("VALID\n")
			sol += index
		index += 1
		'''
		packets.append(left)
		packets.append(right)
		try:
			input()
		except EOFError:
			break
	packets.append([[2]])
	packets.append([[6]])
	sorted_packets = sort(packets)
	for i in range(len(sorted_packets)):
		if sorted_packets[i] == [[2]] or sorted_packets[i] == [[6]]:
			sol *= i+1
		
	print(sol)
if __name__ == '__main__':
	main()