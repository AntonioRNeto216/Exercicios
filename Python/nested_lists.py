data = dict()
scores = list()
for _ in range(int(input())):
    name = input()
    score = float(input())
    data[name] = score
    scores.append(score)
data = dict(sorted(data.items(), key=lambda x: x[0]))
scores = sorted(set(scores))
for n, v in data.items():
    if v == scores[1]:
        print(n)
