def solution(triangle):
    if len(triangle) == 1:
        return triangle[0][0]
    
    arr = list()
    
    for i in range(len(triangle)):
        if i == 0:
            temp = triangle[i]
        else:
            temp = list()
            for j in range(i+1):
                if j == 0:
                    temp.append(triangle[i][0] + arr[0])
                elif j == i:
                    temp.append(triangle[i][-1] + arr[-1])
                else:
                    temp.append(triangle[i][j] + max(arr[j-1], arr[j]))
                    
        arr = temp
    
    answer = max(arr)
    return answer