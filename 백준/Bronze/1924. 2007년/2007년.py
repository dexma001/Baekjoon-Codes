# 2007
# 2007 Doomsday = WED

m, d = map(int, input().split())

d_arr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if m == 1:
    e = d
else:
    e = sum(d_arr[:m-1]) + d

a = e % 7

answer_arr = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
print(answer_arr[a])
