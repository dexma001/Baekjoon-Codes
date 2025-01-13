arr = list(map(int, input().split()))

bob = float(sum(arr) / 20)

if arr.index(20) == 0:
    alice = float((arr[0]+arr[1]+arr[-1]) / 3)

elif arr.index(20) == 19:
    alice = float((arr[-1] + arr[-2] + arr[0]) / 3)

else:
    alice = float(
        (arr[arr.index(20)] + arr[arr.index(20)-1] + arr[arr.index(20)+1])/3)

if bob > alice:
    print('Bob')
elif alice > bob:
    print('Alice')
else:
    print('Tie')
