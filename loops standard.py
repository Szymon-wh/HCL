from sys import stdin, stdout



def loops():
    #n = int(stdin.readline())
    x, n = [int(x) for x in stdin.readline().split()]
    iteracja = 0
    if n <= 0:
        pass
    else:
        while iteracja <= (n - 1):
            iteracja += 1
            score = x*iteracja
            #print(type(score))
            stdout.writelines(str(score))
            stdout.write("\n")

loops()
