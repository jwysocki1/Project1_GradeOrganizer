#This is the second class lab, which I built my program off of.
num_students = int(input("Enter total number of students: "))
scores = input(f"Enter {num_students} scores: ").split()

scores = scores[:num_students]
scores = [int(x) for x in scores]
best = max(scores)

if len(scores) < num_students:
    while len(scores) != num_students:
        scores.append(best-50)

for n in range(num_students):
    if scores[n] >= (best-10):
        print(f'Student {n+1}\'s score is {scores[n]} and their grade is an A.')
    elif scores[n] >= (best-20):
        print(f'Student {n+1}\'s score is {scores[n]} and their grade is a B.')
    elif scores[n] >= (best-30):
        print(f'Student {n+1}\'s score is {scores[n]} and their grade is a C.')
    elif scores[n] >= (best-40):
        print(f'Student {n+1}\'s score is {scores[n]} and their grade is a D.')
    else:
        print(f'Student {n+1}\'s score is {scores[n]} and their grade is a F.')