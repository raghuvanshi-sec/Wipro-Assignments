start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

d = {}

for i in range(start, end + 1):
    d[i] = i * i

print("Dictionary:")
print(d)