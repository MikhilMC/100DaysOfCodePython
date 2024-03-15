student_scores = input("Input a list of student scores : ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

# Write your code below this row 👇
high_score = student_scores[0]
for n in range(1, len(student_scores)):
  if high_score < student_scores[n]:
    high_score = student_scores[n]

print(f"The highest score in the class is: {high_score}")