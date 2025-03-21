# def stone_piles(n):
#     # If n is even, start with 2 and increment by 2
#     if n % 2 == 0:
#         return [2 * (i + 1) for i in range(n - 1)]
    
#     # If n is odd, start with 1 and increment by 2
#     else:
#         return [2 * i + 1 for i in range(n - 1)]

# # Test cases
# print(stone_piles(7))  # Should output [1, 3, 5]
# print(stone_piles(8))  # Should output [2, 4, 6, 8, 10, 12, 14]

# def stone_piles(n):
#     # First pile has n stones
#     first_pile = n
    
#     # List to store pile sizes
#     piles = []
    
#     # Determine if we're working with odd or even numbers
#     is_odd = n % 2 != 0
    
#     # Current stone count starts from the first pile
#     current = first_pile
    
#     # Create n-1 additional piles
#     for _ in range(n - 1):
#         # If first pile is odd, increment by 2 to keep odd
#         if is_odd:
#             current += 2
#             piles.append(current)
#         # If first pile is even, increment by 2 to keep even
#         else:
#             current += 2
#             piles.append(current)
    
#     return piles

# # Test cases
# print(stone_piles(7))   # Should output [9, 11, 13, 15, 17, 19]
# print(stone_piles(8))   # Should output [10, 12, 14, 16, 18, 20, 22]

# def stones_in_piles(n):
#     if n % 2 == 0:
#         return list(range(2, n + 1, 2))
#     else:
#         return list(range(2, n, 2))

# n = int(input("Enter the number of stones: "))
# print(f"Stones in piles: {stones_in_piles(n)}")

def stone_piles(n):
    """
    Calculates the number of stones in each pile.

    Args:
        n: The total number of stones.

    Returns:
        A list of the number of stones in each pile.
    """

    pile_sizes = []
    initial_size = 2 if n % 2 == 0 else 1
    current_size = initial_size

    while n >= current_size:
        pile_sizes.append(current_size)
        n -= current_size
        current_size += 2 if n % 2 == 0 else 1

    return pile_sizes

# Example usage:
n = 7
result = stone_piles(n)
print("Stones in each pile:", result)
