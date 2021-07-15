s = input()
answer = [False for _ in range(5)]
for letter in s:
    if letter.isalnum():
        answer[0] = True
    if letter.isalpha():
        answer[1] = True
    if letter.isdigit():
        answer[2] = True
    if letter.islower():
        answer[3] = True
    if letter.isupper():
        answer[4] = True
print(*answer, sep="\n")
