string = input("Enter a string: ")

reverse = string[::-1]

if string == reverse:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")