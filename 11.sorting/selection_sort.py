class SelectionSort:
    def sort(self, input: list[str]) -> list[str]:
        for i in range(len(input)):
            smallest_position = i
            for j in range(i+1, len(input)):
                if input[j] < input[smallest_position]:
                    smallest_position = j
            input[i], input[smallest_position] = input[smallest_position], input[i]
        return input


s = SelectionSort()

input = ["b", "c", "d", "a", "e", "f", "z", "y", "w", "h", "g"]
print(f"Selection Sort Result: {s.sort(input)}")

input = [5, 8, 3, 9, 4, 1, 7]
print(f"Selection Sort Result: {s.sort(input)}")
