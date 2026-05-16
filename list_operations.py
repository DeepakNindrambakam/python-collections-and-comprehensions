# List Operations

numbers = [10, 20, 30, 40]

# Add element
numbers.append(50)

# Remove element
numbers.remove(20)

# Sort list
numbers.sort()

print("Updated List:", numbers)

# Slicing
print("First 3 Elements:", numbers[:3])
# Tuple Handling

student = ("Deepak", 20, "B.Tech")

# Access elements
print("Name:", student[0])

# Tuple unpacking
name, age, course = student

print("Age:", age)
print("Course:", course)
# Dictionary Usage

student = {
    "name": "Deepak",
    "age": 20,
    "course": "B.Tech"
}

# Add new key
student["grade"] = "A"

# Update value
student["age"] = 21

print(student)

# Loop through dictionary
for key, value in student.items():
    print(key, ":", value)
    # Set Operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
# List Comprehensions

numbers = [1, 2, 3, 4, 5]

# Squares using list comprehension
squares = [x**2 for x in numbers]

# Even numbers
even_numbers = [x for x in numbers if x % 2 == 0]

print("Squares:", squares)
print("Even Numbers:", even_numbers)
