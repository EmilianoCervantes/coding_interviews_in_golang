import random


class QuicksortNaive:
    def sort(self, arr: list[str]) -> list[str]:
        """
        Check the memory usage.
        """

        if len(arr) < 2:
            return arr

        # Select a pivot
        arbitrary_pivot = arr[0]  # Remember this is arbitrary

        left_side = []
        pivot_arr = []
        right_side = []

        for value in arr:
            if value < arbitrary_pivot:
                left_side.append(value)
            elif value > arbitrary_pivot:
                right_side.append(value)
            else:
                pivot_arr.append(value)

        return self.sort(left_side) + pivot_arr + self.sort(right_side)


class QuicksortLomuto:
    def helper(self, arr: list[str], start: int, end: int):
        if start >= end:
            return

        random_index = random.randint(start, end)
        # Swap the random pivot with the first element
        arr[start], arr[random_index] = arr[random_index], arr[start]
        pivot = arr[start]

        pointer = start  # Points to the first bigger than pivot value found
        # Keep in mind, if we were to use the last elem as pivot, pointer = start - 1

        for i in range(start+1, end+1):
            if arr[i] < pivot:
                # Check for smaller elements
                # there is none bigger to the left
                pointer += 1

                # Avoid many unnecessary self swaps
                if i != pointer:
                    arr[i], arr[pointer] = arr[pointer], arr[i]

        # Swap pivot with the right most smaller value
        arr[start], arr[pointer] = arr[pointer], arr[start]

        self.helper(arr, start, pointer-1)
        self.helper(arr, pointer+1, end)

    def sort(self, arr: list[str]) -> list[str]:
        """
        Using pointers for this.
        """
        self.helper(arr, 0, len(arr)-1)

        return arr


class QuicksortHoare:
    def helper(self, arr: list[str], start: int, end: int):
        if start >= end:
            return

        random_index = random.randint(start, end)
        arr[start], arr[random_index] = arr[random_index], arr[start]
        pivot = arr[start]

        left_pointer = start+1
        right_pointer = end

        # With <= we guarantee that the right pointer will go over to the left side
        while left_pointer <= right_pointer:
            if arr[left_pointer] < pivot:
                left_pointer += 1
            elif arr[right_pointer] > pivot:
                right_pointer -= 1
            else:
                # We reached values we need to switch
                arr[left_pointer], arr[right_pointer] = arr[right_pointer], arr[left_pointer]
                left_pointer += 1
                right_pointer -= 1

        arr[start], arr[right_pointer] = arr[right_pointer], arr[start]

        self.helper(arr, start, right_pointer-1)
        self.helper(arr, right_pointer+1, end)

    def sort(self, arr: list[str]) -> list[str]:
        self.helper(arr, 0, len(arr)-1)

        return arr


# q = QuicksortNaive()

# arr = ["b", "c", "d", "a", "b", "a", "e",
#        "f", "z", "a", "y", "w", "h", "g", "y"]
# print(f"Quicksort - Naïve Approach Result: {q.sort(arr)}")

# arr = [5, 8, 3, 9, 4, 1, 7]
# print(f"Quicksort - Naïve Approach Result: {q.sort(arr)}")

# print("\n----- ----- -----")
# print("----- ----- -----\n")

# q = QuicksortLomuto()

# arr = ["b", "c", "d", "a", "b", "a", "e",
#        "f", "z", "a", "y", "w", "h", "g", "y"]
# print(
#     f"Quicksort - Lomuto's Partitioning Result: {q.sort(arr)}")

# arr = [4, 2, 8, 7, 1, 3, 5, 6]
# print(
#     f"Quicksort - Lomuto's Partitioning Result: {q.sort(arr)}")

# print("\n----- ----- -----")
# print("----- ----- -----\n")

q = QuicksortHoare()

arr = ["b", "c", "d", "a", "b", "a", "e",
       "f", "z", "a", "y", "w", "h", "g", "y"]
print(f"Quicksort - Hoare's Partitioning Result: {q.sort(arr)}")

arr = [5, 8, 3, 9, 4, 1, 7]
print(f"Quicksort - Hoare's Partitioning Result: {q.sort(arr)}")
