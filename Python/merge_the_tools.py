def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub_string = ""
        for j in range(0, k):
            if string[i+j] not in sub_string:
                sub_string += string[i+j]
        print(sub_string)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)