names = []
scores = []

while True:
    name = input("Enter student name (or done to finish):")
    if name == "done":
        break
    names.append(name)

    score = int(input("Enter score: "))
    scores.append(score)

for i in range(len(names)):
    print(names[i], ":", scores[i])


average = sum(scores)/len(scores)
print(average)

lowest = min(scores)
print("Lowest: ", scores)

highest = max(scores)
print("Highest: ", highest)
  










