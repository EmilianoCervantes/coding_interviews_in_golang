class BubbleSort:
    def sort(self, input: list[str]) -> list[str]:
        for i in range(len(input)):
            for j in range(len(input) - 1, i, -1):
                # right < left
                if input[j] < input[j-1]:
                    input[j-1], input[j] = input[j], input[j-1]
        return input


b = BubbleSort()

input = ["b", "c", "d", "a", "e", "f", "z", "y", "w", "h", "g"]
print(f"Bubble Sort Result: {b.sort(input)}")

input = [5, 8, 3, 9, 4, 1, 7]
print(f"Bubble Sort Result: {b.sort(input)}")
