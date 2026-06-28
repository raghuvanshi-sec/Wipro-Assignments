def sum_list(numbers):
    return sum(numbers)

n = int(input("Enter the number of elements: "))

lst = []

for i in range(n):
    num = int(input("Enter element: "))
    lst.append(num)

result = sum_list(lst)

print("Sum =", result)