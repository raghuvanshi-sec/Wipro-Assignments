numbers = [10, 20, 30, 40]

print("Original List:", numbers)

item = int(input("Enter a new element: "))

numbers.insert(1, item)

# pyrefly: ignore [parse-error]
print("Updated List:", numbers)