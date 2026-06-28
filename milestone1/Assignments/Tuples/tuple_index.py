n = int(input("Enter the number of elements: "))

lst = []
for i in range(n):
    element = input("Enter element: ")
    lst.append(element)

t = tuple(lst)

print("Tuple:", t)

item = input("Enter element to find index: ")

if item in t:
    print("Index:", t.index(item))
else:
    print("Element not found.")