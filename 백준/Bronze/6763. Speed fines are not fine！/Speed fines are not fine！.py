n = int(input())
m = int(input())

if m <= n:
    print("Congratulations, you are within the speed limit!")
else:
    if m-n <= 20:
        print('You are speeding and your fine is $100.')
    elif m-n <= 30:
        print('You are speeding and your fine is $270.')
    else:
        print('You are speeding and your fine is $500.')
