import sys

input = sys.stdin.readline

def solve():
    T = int(input())
    
    for _ in range(T):
        a, b, c, d = map(int, input().split())
        same_x = ((a & 4) == (b & 4) == (c & 4) == (d & 4))
        
        same_y = ((a & 2) == (b & 2) == (c & 2) == (d & 2))
        
        same_z = ((a & 1) == (b & 1) == (c & 1) == (d & 1))
        
        if same_x or same_y or same_z:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()