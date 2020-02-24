def loops():
    x, n = [int(x) for x in input("Write two numbers: ").split()]
    """x = int(w)
    n = int(z)"""
    iteracja = 0
    if n <= 0:
        pass
    else:
        while iteracja <= (n - 1):
            iteracja += 1
            score = x * iteracja
            print(score)


loops()