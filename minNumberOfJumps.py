"""
Another classic dynamic problem
I solved this by myself! Without looking at an explanation
"""

def minNumberOfJumps(array):
	# takes 0 steps to go from the final index to the final index
	array[-1] = 0
	# iterate through the array backwards
    for i in range(len(array) - 2, -1, -1):
		# the furthest location we can jump to from i
		max_jump = i + array[i]
		#print(i, array[i], max_jump)
		# can jump straight to the final index
		if max_jump >= len(array) - 1:
			array[i] = 1
		else:
			min_idx = i + 1
			
			# find the location it can jump to with the least
			# number of jumps to the end
			for j in range(i + 2, max_jump + 1, 1):
				if array[j] < array[min_idx]:
					min_idx = j
					
					# no other location can be more optimal
					if array[min_idx] == 1:
						break
			array[i] = array[min_idx] + 1
		#print(array)
	# return the smallest number of steps from the start to end
	return array[0]
