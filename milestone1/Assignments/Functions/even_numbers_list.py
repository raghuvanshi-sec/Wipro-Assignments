def even_numbers(lst):
    even = []

    for num in lst:
        if num % 2 == 0:
            even.append(num)

    print("Even Numbers:", even)

n = int(input("Enter the number of elements: "))

numbers = []

for i in range(n):
    value = int(input("Enter element: "))
    numbers.append(value)

even_numbers(numbers)