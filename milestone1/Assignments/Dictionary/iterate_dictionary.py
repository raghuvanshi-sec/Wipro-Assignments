d = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

print("\nKeys:")
for key in d:
    print(key)

print("\nValues:")
for value in d.values():
    print(value)

print("\nKeys and Values:")
for key, value in d.items():
    print(key, ":", value)