n1 = int(input("Enter the number of elements in Set 1: "))

set1 = set()

for i in range(n1):
    element = input("Enter element: ")
    set1.add(element)

n2 = int(input("\nEnter the number of elements in Set 2: "))

set2 = set()

for i in range(n2):
    element = input("Enter element: ")
    set2.add(element)

print("Set 1:", set1)
print("Set 2:", set2)

union = set1.union(set2)

print("Union of the sets:", union)