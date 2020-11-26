def minion_game(string):
    vogais = ["A", "E", "I", "O", "U"]
    string = string.upper()
    stuart_score = 0
    kevin_score = 0
    num = len(string)
    for letra in string:
        if letra in vogais:
            kevin_score += num
        else:
            stuart_score += num
        num -= 1
    if stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    elif kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)