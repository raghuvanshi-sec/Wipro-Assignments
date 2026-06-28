n = int(input("Enter the number of elements in the set: "))

s = set()

for i in range(n):
    element = int(input("Enter element: "))
    s.add(element)

print("Set:", s)

print("Maximum value:", max(s))
print("Minimum value:", min(s))