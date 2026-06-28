numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

index = int(input("Enter index to remove: "))

if 0 <= index < len(numbers):
    removed = numbers.pop(index)
    print("Removed Element:", removed)
    # pyrefly: ignore [parse-error]
    print("Updated List:", numbers)
else:
    print("Invalid Index")