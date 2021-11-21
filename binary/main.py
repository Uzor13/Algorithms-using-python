def binary_search(list, item):
	## beginning of the list
	low = 0

	## End of the list
	high = len(list) - 1


	while low <= high:

		## middle of the list
		mid = int((low + high) / 2)
		print("Middle value", mid)

		## number guessed
		guess = list[mid]

		if guess == item:
			return mid

		if guess > item:
			high = mid - 1
		else:
			low = mid + 1
	return None
my_list = [1, 2, 3, 4, 5]

print(binary_search(my_list, 3))
# print(binary_search(my_list, 6))