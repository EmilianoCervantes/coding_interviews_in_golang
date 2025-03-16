class InsertionSort:
    def sort_deprecated(self, input: list[str]) -> list[str]:
        """
        This solution is done with **Swaps**.
        In terms of memory efficiency, it's not very good.
        There are more writes. That's the nature of swaps.

        If you translate this to a large dataset.
        And with complex values.
        You might understand why.
        """
        for i in range(1, len(input)):
            is_lower = True
            curr_left_pos = i
            while is_lower:
                if input[curr_left_pos] < input[curr_left_pos-1]:
                    input[curr_left_pos], input[curr_left_pos -
                                                1] = input[curr_left_pos-1], input[curr_left_pos]
                    curr_left_pos -= 1
                else:
                    is_lower = False

                if curr_left_pos == 0:
                    is_lower = False

        return input

    def sort(self, input: list[str]) -> list[str]:
        for i in range(1, len(input)):
            # We need this temp variable,
            # try to do without it and you'll have some bugs.
            curr_value = input[i]
            curr_left_pos = i - 1
            while curr_left_pos > -1 and curr_value < input[curr_left_pos]:
                input[curr_left_pos+1] = input[curr_left_pos]
                curr_left_pos -= 1
            input[curr_left_pos+1] = curr_value

        return input


i = InsertionSort()

input = ["b", "c", "d", "a", "e", "f", "z", "y", "w", "h", "g"]
print(f"Insertion Sort Result: {i.sort(input)}")

input = [5, 8, 3, 9, 4, 1, 7]
print(f"Insertion Sort Result: {i.sort(input)}")
