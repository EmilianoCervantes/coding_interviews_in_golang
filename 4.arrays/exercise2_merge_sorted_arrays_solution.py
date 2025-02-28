"""
Description:
Given 2 sorted arrays
Merge them and keep the resulting array sorted
"""

# // Step 1: accept 2 arrays
"""
What kind of arrays do we take?
Usually you get an example and you can ask if you can assume the arrays will be of that type.
Ex: [0,3,4,31] and [4,6,30]
And based on the description, we want to return a sorted array
"""

def merge_sorted_arrays_solution(arr1: list[int], arr2: list[int]) -> list[int]:
		# Let's create a slice that we will return
		sorted_result: list[int] = []

		# We don't know the length of each array, either could be smaller than the other
		# So let's just traverse through the first array
		# What I'll do next is compare number by number between the arrays
		# and insert them in the new array based on which number is smaller
		# For that I'll need an extra pointer to know which position I'm pointing at in the second array
		arr1_position = 0
		arr2_position = 0

		# What happens in any of those 2 arrays is empty?
		# Then the for will never happen
		if len(arr1) < 1:
				return arr2

		if len(arr2) < 1:
				return arr1

		while arr1_position < len(arr1) and arr2_position < len(arr2): # O(n+m)
				valueArr1 = arr1[arr1_position]
				valueArr2 = arr2[arr2_position]
				if valueArr1 < valueArr2: # 0 is less than 4
						sorted_result.append(valueArr1)
						arr1_position += 1

				# Note: we could simplify the last 2 elses, how and why?
				elif valueArr1 > valueArr2: # When 6 is less than 31
						sorted_result.append(valueArr2)
						arr2_position += 1
				else: # When 4 == 4
						sorted_result.extend([valueArr1, valueArr2])
						arr1_position += 1
						arr2_position += 1

				# Now what happens if len(arr1) > len(arr2) ?
				# That means we no longer have anything to compare
				# We cans skip to add the rest of the array #1 to the sorted results
				# I'll check this by seeing if we already reached the end of the array 2
				if arr2_position == len(arr2):
						sorted_result.extend(arr1[arr1_position:])
						break

				# And if len(arr1) < len(arr2)
				# This means we didn't finish adding the values of arr2
				# We will add the rest of the array #2 to the sorted results
				if arr1_position == len(arr1):
						sorted_result.extend(arr2[arr2_position:])

		return sorted_result

arr1 = [1,3,5,7,9,11,13,15]
arr2 = [2,3,4,6,8,10]

print("merge_sorted_arrays_solution", merge_sorted_arrays_solution(arr1, arr2))
