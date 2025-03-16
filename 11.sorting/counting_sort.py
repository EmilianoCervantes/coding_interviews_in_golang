class CountingSort:
    def sort(self, arr: list[int]) -> list[int]:
        if len(arr) == 0:
            return []

        # [value, repetitions]
        arr_as_dict: dict[int, int] = {}
        res = []

        max_value = max(arr)
        min_value = min(arr)

        for value in arr:
            if value not in arr_as_dict:
                arr_as_dict[value] = 1
            else:
                arr_as_dict[value] += 1

        # Go from min_value to max_value
        for num in range(min_value, max_value+1):
            if num in arr_as_dict:
                repetitions = arr_as_dict[num]
                for _ in range(repetitions):
                    res.append(num)
        return res


c = CountingSort()

arr = [9, 6, 3, 5, 2, 1, 2]
print(f"Counting Sort Result: {c.sort(arr)}")

arr = [5, 8, 3, 9, 4, 1, 7]
print(f"Counting Sort Result: {c.sort(arr)}")

arr = [4, 2, 8, 7, 1, 3, 5, 6]
print(f"Counting Sort Result: {c.sort(arr)}")
