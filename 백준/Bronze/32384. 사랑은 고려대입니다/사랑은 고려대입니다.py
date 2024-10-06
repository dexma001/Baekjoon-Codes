n = int(input())
if n == 1:
    print("LoveisKoreaUniversity")

else:
    temp = str("LoveisKoreaUniversity")
    for _ in range(n-1):
        temp += ' LoveisKoreaUniversity'

    print(temp)
