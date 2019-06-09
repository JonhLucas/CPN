def sum_10(lis, begin, end, total):
    middle = int((end+begin) / 2)
    x = lis[begin]
    a = 0
    b = 100000000
    #print("inicio: %i - meio: %i - fim %i - total: %i" % (begin, middle, end, total))
    if begin < middle:
        #print('------------', begin, middle, end, x + lis[middle])
        if (x + lis[middle]) == total:
            a = x
            b = lis[middle]
            #print('encontrado')
        elif (x + lis[middle]) > total:
            #print('middle <-', begin, middle)
            e, f = sum_10(lis, begin, middle, total)
            if (int(f) - int(e) < b - a) and (f + x == total):
                b = int(f)
                a = int(e)
                #print('novos valores', a, b)
        else:
            #print('middle ->', middle, end)
            e, f = sum_10(lis, middle, end, total-x+lis[middle])
            if (int(f) - x < b - a) and (f + x == total):
                b = int(f)
                a = x
                #print('novos valores', a, b)
        x = lis[begin]
    #print('resultado: ', a, b)
    return a, b


def launcher(lista, inicio, fim, soma):
    x1 = 0
    x2 = 100000000
    while inicio < fim-1:
        #print('novo ciclo. begin =', inicio)
        inter1, inter2 = sum_10(lista, inicio, fim, soma)
        if inter2 - inter1 < x2 - x1 and inter2 + inter1 == soma:
           x2 = inter2
           x1 = inter1
        inicio += 1
    return x1, x2


while True:
    try:
        size = int(input())
        a1 = []
        a1 = input().split()
        total1 = int(input())
        a1 = list(map(int, a1))
        a1.sort()
        v1, v2 = launcher(a1, 0, size, total1)
        print('RESULTADO FINAL:', v1, v2)
    except EOFError:
        break
