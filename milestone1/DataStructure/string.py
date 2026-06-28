s = input("Enter a string: ").lower()
sub = input("Enter substring: ").lower()

count = 0
start = 0

while True:
    pos = s.find(sub, start)
    if pos != -1:
        count += 1
        start = pos + 1
    else:
        break

print("Number of times substring appears:", count)