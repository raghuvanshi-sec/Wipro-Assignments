# Input the three strings
string1 = input("Enter liked numbers (hyphen-separated): ")
string2 = input("Enter disliked numbers (hyphen-separated): ")
string3 = input("Enter given numbers (hyphen-separated): ")

# Convert strings into lists
liked = string1.split("-")
disliked = string2.split("-")
given = string3.split("-")

happiness = 0

# Calculate happiness
for num in given:
    if num in liked:
        happiness += 1
    elif num in disliked:
        happiness -= 1

print("Final Happiness:", happiness)