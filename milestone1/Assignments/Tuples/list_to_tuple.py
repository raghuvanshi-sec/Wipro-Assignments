n = int(input("Enter the number of elements in the list: "))

lst = []
for i in range(n):
    element = input("Enter element: ")
    lst.append(element)

print("List:", lst)

t = tuple(lst)

print("Tuple:", t)