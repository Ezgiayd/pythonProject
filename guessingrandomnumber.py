from random import randint
x= randint(0,10)
print(x)
while True:
    a = int(input('input your guess'))
    if a>x:
        print('the x is smaller')
    elif a<x:
        print('the x is bigger')
    else:
        print('you found the number')
        break






