n = int(input("Enter the number of tuples: "))

tuple_list = []

for i in range(n):
    size = int(input(f"\nEnter number of elements in tuple {i+1}: "))
    temp = []

    for j in range(size):
        value = int(input("Enter element: "))
        temp.append(value)

    tuple_list.append(tuple(temp))

print("\nOriginal List:")
print(tuple_list)

result = []

for t in tuple_list:
    t = t[:-1] + (100,)
    result.append(t)

print("\nUpdated List:")
print(result)