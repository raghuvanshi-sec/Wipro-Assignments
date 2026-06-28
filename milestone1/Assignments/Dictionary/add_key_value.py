d = {}

n = int(input("Enter the number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

print("Dictionary:", d)

new_key = input("Enter new key: ")
new_value = int(input("Enter new value: "))

d[new_key] = new_value

print("Updated Dictionary:", d)