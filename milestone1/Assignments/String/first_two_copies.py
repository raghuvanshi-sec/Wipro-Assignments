string = input("Enter a string: ")

if len(string) >= 2:
    result = string[:2] * len(string)
    print("Output:", result)
else:
    print("String length should be at least 2.")