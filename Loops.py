def loops ():
    print('Write two numbers:')
    x = int(input())
    n = int(input())
    iteracja = 0
    if n == 0:
        print('0')
    else:
        while iteracja <= (n-1):
            iteracja += 1
            score = x*iteracja
            print(score)

loops()