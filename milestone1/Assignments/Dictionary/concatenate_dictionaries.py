dic1 = {}
dic2 = {}
dic3 = {}

n1 = int(input("Enter number of elements in Dictionary 1: "))
for i in range(n1):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic1[key] = value

n2 = int(input("\nEnter number of elements in Dictionary 2: "))
for i in range(n2):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic2[key] = value

n3 = int(input("\nEnter number of elements in Dictionary 3: "))
for i in range(n3):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    dic3[key] = value

result = {}
result.update(dic1)
result.update(dic2)
result.update(dic3)

print("Concatenated Dictionary:")
print(result)