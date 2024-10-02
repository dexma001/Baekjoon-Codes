import sys
import re
code = sys.stdin.readlines()

for i in code:
    while True:
        res = re.sub('BUG', '', i)

        if 'BUG' in res:
            i = res
        else:
            print(res, end="")
            break
