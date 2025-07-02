arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
point = [13, 7, 5, 3, 3, 2]

cocjr0208 = 0
ekwoo = 1.5

for i in range(6):
    cocjr0208 += arr1[i] * point[i]
    ekwoo += arr2[i] * point[i]

print("ekwoo") if max(cocjr0208, ekwoo) == ekwoo else print("cocjr0208")
