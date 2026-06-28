def count_case(string):
    upper = 0
    lower = 0

    for ch in string:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)

text = input("Enter a string: ")

count_case(text)