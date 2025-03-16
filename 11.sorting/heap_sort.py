class HeapSort:
    def __heapify(self, arr, curr_index, len_to_cover):
        """
        len_to_cover is not only used for Building the Max-Heap
        It is used as well when sorting.

        That's why using directly len(arr) is not the best,
        we need to pass the length we wanna check dynamically.

        Refer to the README#in-place-heap-sort for more.
        """
        index_largest = curr_index  # Lets see which element is the largest
        #  Children are i*2 and i*2+1
        # Check both sides and pick the largest
        left_child_index = curr_index*2+1  # E.g. 0*2 = 0 + 1 = 1
        right_child_index = curr_index*2+2

        # Remember: '<' error for IndexError: list index out of range
        # Validation in case parent doesn't have a right children
        if right_child_index < len_to_cover and arr[right_child_index] > arr[index_largest]:
            index_largest = right_child_index
        # "left_child_index < len_to_cover" is needed because we are going to do this check recursively
        if left_child_index < len_to_cover and arr[left_child_index] > arr[index_largest]:
            index_largest = left_child_index

        if index_largest != curr_index:
            arr[curr_index], arr[index_largest] = arr[index_largest], arr[curr_index]
            self.__heapify(arr, index_largest, len_to_cover)

    def sort(self, arr: list[str]):
        # First Build the Max-Heap
        # Parents are n/2
        # First parent
        start_index = len(arr) // 2
        for i in range(start_index, -1, -1):
            self.__heapify(arr, i, len(arr))

        # Max-Heap is done
        # Next sort it
        for i in range(len(arr)-1, -1, -1):
            # Swap max element with last element
            # Review the Readme#in-place-heap-sort for more.
            arr[0], arr[i] = arr[i], arr[0]
            self.__heapify(arr, 0, i)
        return arr


h = HeapSort()

arr = ["b", "c", "d", "a", "b", "a", "e",
       "f", "z", "a", "y", "w", "h", "g", "y"]
print(f"Heap Sort Result: {h.sort(arr)}")

arr = [5, 8, 3, 9, 4, 1, 7]
print(f"Heap Sort Result: {h.sort(arr)}")

arr = [4, 2, 8, 7, 1, 3, 5, 6]
print(f"Heap Sort Result: {h.sort(arr)}")
