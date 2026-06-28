numbers = [10, 20, 30, 20, 40, 20, 50]

print("Original List:", numbers)

item = int(input("Enter element to remove: "))

if item in numbers:
    numbers.remove(item)
    print("Updated List:", numbers)
else:
    print("Element not found.")