import sys
input = sys.stdin.readline

for _ in range(100):
    arr = list()
    for _ in range(5000):
        arr.append(float(input()))
    
    t__s = 0
    _ts_ = 0
    
    for i in arr:
        if 0.25<= i <= 0.75:
            t__s += 1
        else:
            _ts_ += 1
            
    if t__s / _ts_ >= 1.4:
        print("B")
    else:
        print("A")