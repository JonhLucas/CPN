keeper = True


def validade(p):
    g = p[0] >= p[1]
    e = (p[0] < p[1]) and (p[0] == 0)
    g = g or e
    x = p[2] >= p[3]
    y = (p[2] < p[3]) and (p[2] == 0)
    x = x or y
    return g and x


def vitoria(p):
    return p == [0, 0, 3, 3]


def ida(place, l1, l2):
    if validade(place):
        local = []
        print("lado esquerdo", place)
        for i in range(3):
            for j in range(3 - i):
                if (i or j) and place[0] >= i and place[1] >= j:
                    new_node = place.copy()
                    new_node[0] -= i
                    new_node[1] -= j
                    new_node[2] += i
                    new_node[3] += j
                    if new_node not in l2 and [0, 0, 3, 3] not in l2:
                        local.append(new_node)
                        l2.append(new_node)
        while len(local) != 0 and [0, 0, 3, 3] not in l2:
            volta(local.pop(0), l1, l2)
    else:
        print("recusado no lado esquerdo:", place)


def volta(place, l1, l2):
    if vitoria(place):
        print("                         Achou")
    elif validade(place):
        local = []
        print("lado direito", place)
        for i in range(3):
            for j in range(3 - i):
                if (i or j) and place[2] >= i and place[3] >= j:
                    new_node = place.copy()
                    new_node[0] += i
                    new_node[1] += j
                    new_node[2] -= i
                    new_node[3] -= j
                    if new_node not in l1:
                        local.append(new_node)
                        l1.append(new_node)
        while len(local) != 0 and [0, 0, 3, 3] not in l2:
            ida(local.pop(0), l1, l2)
    else:
        print("recusado no lado esquerdo:", place)


root = [3, 3, 0, 0]
history = []
l1 = [root]
l2 = []
ida(root, l1, l2)
print("*Lado esquerdo:", l1)
print("*Lado direito:", l2)
