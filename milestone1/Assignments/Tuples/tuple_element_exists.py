n = int(input("Enter the number of elements: "))

lst = []
for i in range(n):
    element = input("Enter element: ")
    lst.append(element)

t = tuple(lst)

search = input("Enter element to search: ")

if search in t:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")