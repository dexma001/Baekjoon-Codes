from itertools import combinations_with_replacement

n, m = map(int, input().split())
li = [i+1 for i in range(n)]

ans = list(combinations_with_replacement(li, m))
for j in range(len(ans)):
    print(*ans[j])