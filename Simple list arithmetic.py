from sys import stdin
def Simple_list_arithmetic():
    n = int(stdin.readline())
    l = []
    if n >= 1 and n <= 500:
        for user in range(0, n):
            ele = int(stdin.readline())
            l.append(ele)

        suma = 0
        for add in range(0, n):
            suma = suma + l[add]
        print(suma)
        #return suma

        difference = l[0]
        for substract in range(1, n):
            difference = difference - l[substract]
        print(difference)
        #return difference

        product = 1
        for increase in range(0, n):
            product = product * l[increase]
        print(product)



        return suma, difference, product
    else:
        print("Wrong number.")

Simple_list_arithmetic()
