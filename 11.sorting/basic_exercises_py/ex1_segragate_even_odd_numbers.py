def segregate_evens_and_odds(numbers: list[int]) -> list[int]:
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    if len(numbers) < 2:
        return numbers
    # We can do a sort of quick or merge sort
    # The pivot would be %2
    even_side = []
    odd_side = []
    for num in numbers:
        if num % 2 == 0:
            even_side.append(num)
        else:
            odd_side.append(num)

    return even_side + odd_side


numbers = [1, 2, 3, 4]

print(f"Segregated numbers: {segregate_evens_and_odds(numbers)}")

numbers = [3, 4]

print(f"Segregated numbers: {segregate_evens_and_odds(numbers)}")
