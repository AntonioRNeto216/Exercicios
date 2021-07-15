def swap_case(s):
    new_s = ""
    for l in s:
        if l.isupper():
            new_s += l.lower()
        else:
            new_s += l.upper()
    return new_s


########### or ##########
def swap_case2(s):
    return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    result2 = swap_case2(s)
    print(result)
    print(result2)
