try:
    filename = input("Enter the file name: ")

    # Add .txt if the user enters only the file name
    if not filename.endswith(".txt"):
        filename += ".txt"

    file = open(filename, "r")

    items = 0
    free_items = 0
    total_amount = 0
    discount = 0

    for line in file:
        line = line.strip()

        # Skip blank lines
        if line == "":
            continue

        data = line.split()

        # Check for discount line
        if data[0].lower() == "discount":
            discount = int(data[1])

        # Check for free item
        elif data[1].lower() == "free":
            free_items += 1

        # Paid item
        else:
            items += 1
            total_amount += int(data[1])

    file.close()

    final_amount = total_amount - discount

    print("No of items purchased:", items)
    print("No of free items:", free_items)
    print("Amount to pay:", total_amount)
    print("Discount given:", discount)
    print("Final amount paid:", final_amount)

except FileNotFoundError:
    print("File not found.")

except ValueError:
    print("Invalid data in file.")

except Exception as e:
    print("Error:", e)