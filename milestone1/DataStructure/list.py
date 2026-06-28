scores = list(map(int, input("Enter the scores separated by spaces: ").split()))

unique_scores = list(set(scores))
unique_scores.sort()

print(unique_scores[-2])