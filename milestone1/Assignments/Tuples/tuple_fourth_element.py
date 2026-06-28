# Enter tuple elements
n = int(input("Enter the number of elements: "))

lst = []
for i in range(n):
    element = input("Enter element: ")
    lst.append(element)

t = tuple(lst)

print("Tuple:", t)

if len(t) >= 4:
    print("4th element from first:", t[3])
    print("4th element from last:", t[-4])
else:
    print("Tuple must contain at least 4 elements.")