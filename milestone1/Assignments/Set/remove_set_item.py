n = int(input("Enter the number of elements in the set: "))

s = set()

for i in range(n):
    element = input("Enter element: ")
    s.add(element)

print("Original Set:", s)

item = input("Enter the element to remove: ")

if item in s:
    s.remove(item)
    print("Updated Set:", s)
else:
    print("Element not found in the set.")