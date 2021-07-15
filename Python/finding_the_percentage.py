n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
scores_sum = 0
for s in student_marks[query_name]:
    scores_sum += s
print(f"{scores_sum / len(student_marks[query_name]):.2f}")
