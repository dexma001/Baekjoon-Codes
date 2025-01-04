n = float(input())
m = float(input())
temp = n/(m*m)

if temp > 25.0:
    print('Overweight')
elif temp < 18.5:
    print('Underweight')
else:
    print('Normal weight')
