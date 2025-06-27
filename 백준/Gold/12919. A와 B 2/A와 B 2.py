#12919

S = str(input())
T = str(input())

answer = 0 
def recursion(string, T):
    global answer
    if answer:
        return 
    if len(string) == len(T):
        if string == T:
            answer = 1
            return 
        else:
            return 
    if T[0] == 'B':
         recursion(string, ''.join(reversed(T[1:])))
    if T[-1] == 'A':
        recursion(string, T[:-1])
    
recursion(S, T)
print(1) if answer else print(0)