string = input("Enter a string: ")
n = int(input("Enter the value of n: "))

if 0 <= n <= len(string):
    result = string[-n:] * n
    print("Output:", result)
else:
    print("Invalid value of n.")