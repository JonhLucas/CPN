def sum_10(list, begin, end, total):
    middle = int((end-begin)/ 2)
    x = list[begin]
    a = 0
    b = 100000000
    while begin < middle:
        print(begin, middle, end)
        if (x + list[middle]) == total:
            a = x
            b = list[middle]
        elif (x + list[middle]) > total:
            e, f = sum_10(list, begin, middle, total)
            if ((int(f) - int(e)) < (b - a)):
                b = int(f)
                a = int(e)
        else:
            e, f = sum_10(list, begin, middle, total)
            if ((int(f) - int(e)) < (b - a)):
                b = int(f)
                a = int(e)
        begin+=1
        middle = int((end-begin)/ 2)
        x = list[begin]
    print('resultado: ',a, b)
    return a,b
while True:
    try:
        size = int(input())
        a = []
        a = input().split()
        total = int(input())
        a = list(map(int, a))
        a.sort()
        x,y = sum_10(a, 0,size, total)
    except EOFError:
        break