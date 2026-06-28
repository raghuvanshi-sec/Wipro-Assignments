d = {}

n = int(input("Enter number of key-value pairs: "))

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

search_key = input("Enter key to search: ")

if search_key in d:
    print("Key exists.")
else:
    print("Key does not exist.")