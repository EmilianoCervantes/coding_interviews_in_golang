class RadixSort:
    def counting_sort(self, arr: list[int], curr_digit: int):
        # [value, repetitions]
        # arr_as_dict: dict[int, int] = {} # Instead of this
        digit_count = [0]*10  # We'll do this
        res = [0]*len(arr)

        for i in range(len(arr)):
            pos = arr[i] // curr_digit % 10
            digit_count[pos] += 1

        for i in range(1, 10):
            digit_count[i] += digit_count[i-1]

        # Process the array from the end to maintain stability
        for i in range(len(arr) - 1, -1, -1):
            pos = arr[i] // curr_digit % 10
            res[digit_count[pos] - 1] = arr[i]
            digit_count[pos] -= 1

        # Update the reference
        # To not make the scope of the change local
        for i in range(len(arr)):
            arr[i] = res[i]

    def sort(self, arr: list[int]):
        # We need to go digit by digit
        longest_num = max(arr)
        curr_digit = 1  # 1, 10, 100, 1000, etc... We'll go digit by digit

        while longest_num // curr_digit > 0:
            self.counting_sort(arr, curr_digit)
            curr_digit *= 10


r = RadixSort()

arr = [21, 345, 13, 101, 50, 234, 1]
r.sort(arr)
print(f"Radix Sort Result: {arr}")

arr = [5, 8, 3, 9, 4, 1, 7]
r.sort(arr)
print(f"Radix Sort Result: {arr}")
