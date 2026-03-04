from collections import defaultdict
import sys
input = sys.stdin.readline

q = 0
while True:
    try:
        n = int(input())
        arr = defaultdict(int)
        
        ttemp = ''    
        while True:
            temp = list(map(str, input().strip()))
            if not temp:
                continue
            
            if ''.join(temp) == "EndOfText":
                break
            
            for i in temp:
                if i.isalpha():
                    ttemp += i.lower()
                else:
                    if ttemp:
                        arr[ttemp] += 1
                        ttemp = ''
                        
            if ttemp:
                    arr[ttemp] += 1
                    ttemp = ''


        ans = list(arr.items())
        ans.sort(key=lambda x:[x[1], x[0]])
        
        if q:
            print("")
        
        t = 0
        for i in ans:
            if i[1] == n:
                print(i[0])    
                t += 1

        if not t:
            print("There is no such word.")
            
        q += 1  

    except:
        break