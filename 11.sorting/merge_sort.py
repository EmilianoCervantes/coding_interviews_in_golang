class MergeSort:
    def __merge(self, left_input: list[str], right_input: list[str]) -> list[str]:
        pointer_left, pointer_right = 0, 0
        helper_arr = []

        # If you do "or" instead of the "and",
        # don't forget to do validations for "None"
        while pointer_left < len(left_input) and pointer_right < len(right_input):
            if left_input[pointer_left] < right_input[pointer_right]:
                helper_arr.append(left_input[pointer_left])
                pointer_left += 1
            else:
                helper_arr.append(right_input[pointer_right])
                pointer_right += 1

        helper_arr.extend(left_input[pointer_left:])
        helper_arr.extend(right_input[pointer_right:])

        return helper_arr

    def sort(self, input: list[str]) -> list[str]:
        # Base case - nothing else to divide
        if len(input) < 2:
            return input

        # Divide array in halves
        middle_index = len(input) // 2

        # Keep dividing in halves
        # Then do sort for both halves
        return self.__merge(self.sort(input[:middle_index]), self.sort(input[middle_index:]))


m = MergeSort()

input = ["b", "c", "d", "a", "a", "e", "f", "z", "a", "y", "w", "h", "g", "y"]
print(f"Merge Sort Result: {m.sort(input)}")

input = [5, 8, 3, 9, 4, 1, 7]
print(f"Merge Sort Result: {m.sort(input)}")
