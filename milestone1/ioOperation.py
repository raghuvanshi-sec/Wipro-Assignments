import string

# Get filename from user
filename = input("Enter the file name: ")

try:
    with open(filename, "r") as file:
        lines = file.readlines()

    # Count number of lines
    line_count = len(lines)

    # Determine meeting time
    if line_count == 0:
        print("The file is empty.")
    else:
        if line_count == 12:
            meeting_time = "12 PM"
        elif line_count > 12:
            meeting_time = str(line_count - 12) + " PM"
        else:
            meeting_time = str(line_count) + " AM"

        # Count frequency of words
        words = {}

        for line in lines:
            line = line.lower()
            line = line.translate(str.maketrans("", "", string.punctuation))
            for word in line.split():
                words[word] = words.get(word, 0) + 1

        # Find the most frequent word
        meeting_place = max(words, key=words.get)

        print("Meeting time:", meeting_time)
        print("Meeting place:", meeting_place.capitalize(), "Street")

except FileNotFoundError:
    print("File not found.")