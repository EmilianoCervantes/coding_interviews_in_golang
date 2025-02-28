from typing import Optional

"""
Given a certain string, return it backwards.
"""

def reverse_a_string_solution(text: Optional[str] = None) -> str: # Time complexity is O(n)
		"""
		Step 1 - I would expect a string as a param and return another string

		As an extra, with Optional[str] we give the function right away the possibility of being receiving or not anything.
		Giving more freedom to whoever calls this function.

		Also, Python has a lot of freedom with parameters, so I'm making use of Python 3.5 to add typing.
		That way making our code less prone to mistakes.
		"""

		reversedString = ""

		# Step 2 - if we have only 1 letter or the string is empty, we don't need to do any operations
		if text == None:
				return ""

		if len(text) < 2:
				return text

		# Step 3 - go over the string letter by letter
		# Note: you might think of doing this:
		for char in text: # Time complexity is O(n)
				reversedString = char + reversedString
		# Finally, return the string backwards
		return reversedString

"""
What will be the result of the next examples:
"""

test1 = "Hi you"
print(f"{test1}:", reverse_a_string_solution(test1))
test2 = "Hey\tyou there"
print(f"{test2}:", reverse_a_string_solution(test2))
print(f"{None}:", reverse_a_string_solution())
