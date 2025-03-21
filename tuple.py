# Creating a tuple
coordinates = (10, 20)
person = ('Alice', 30, 'New York')

# Accessing elements
print(coordinates[0])  # Output: 10
print(person[-1])  # Output: New York

# Tuple unpacking
name, age, city = person
print(f"{name} is {age} years old and lives in {city}")

# Attempting to modify a tuple will raise an error
# coordinates[0] = 15  # This would raise a TypeError

# Tuple methods
print(coordinates.count(10))  # Output: 1
print(person.index('Alice'))  # Output: 0

# Tuples are often used for multiple return values
def get_dimensions():
    return (1920, 1080)

width, height = get_dimensions()
print(f"Width: {width}, Height: {height}")

# Tuples can be used as dictionary keys (unlike lists)
point_values = {(0, 0): 100, (1, 1): 200}
print(point_values[(1, 1)])  # Output: 200