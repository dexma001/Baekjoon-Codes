n = int(input())
temp = list(map(str, input().split('*')))
temp_len = len(temp[0]) + len(temp[1])

for _ in range(n):
    string = list(map(str, input().strip()))
    if len(string) >= temp_len and ''.join(string[:len(temp[0])]) == temp[0] and ''.join(string[len(string) - len(temp[1]):]) == temp[1]:
        print("DA")
    else:
        print("NE")
    