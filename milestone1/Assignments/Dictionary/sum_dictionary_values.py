d = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

total = sum(d.values())

print("Dictionary:", d)
print("Sum of all values:", total)