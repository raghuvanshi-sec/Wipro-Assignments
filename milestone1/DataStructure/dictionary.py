people = {}

# Input number of people
n = int(input("Enter the number of people: "))

# Input names and facts
for i in range(n):
    name = input("Enter person's name: ")
    fact = input("Enter an interesting fact: ")
    people[name] = fact

print("\nOriginal Dictionary:")
for person, fact in people.items():
    print(person + ": " + fact)

# Update a fact
update_name = input("\nEnter the name whose fact you want to change: ")

if update_name in people:
    new_fact = input("Enter the new fact: ")
    people[update_name] = new_fact
else:
    print("Person not found.")

# Add a new person
new_name = input("\nEnter the new person's name: ")
new_fact = input("Enter the interesting fact: ")
people[new_name] = new_fact

# Display updated dictionary
print("\nUpdated Dictionary:")
for person, fact in people.items():
    print(person + ": " + fact)