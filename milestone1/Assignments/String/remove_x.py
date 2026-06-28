string = input("Enter a string: ")

if len(string) > 0 and string[0] == 'x':
    string = string[1:]

if len(string) > 0 and string[-1] == 'x':
    string = string[:-1]

print("Output:", string)