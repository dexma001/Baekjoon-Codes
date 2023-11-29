# 1043

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
li_know_trust = set(map(int, input().split()[1:]))

party_list = list()

for _ in range(m):
    party_people = list(map(int, input().split()))
    party_list.append(set(party_people[1:]))

for _ in range(m):
    for j in range(len(party_list)):
        if party_list[j] & li_know_trust:
            li_know_trust = li_know_trust.union(party_list[j])

cnt = 0

for k in range(len(party_list)):
    if li_know_trust & party_list[k]:
        continue
    cnt += 1

print(cnt)
