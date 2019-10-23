def part(node, l):
    new = node.copy()
    if new[0] >= 2:
        new[0] -= 2
        new[2] = new[0] + new[1]
        new[3] += 2
        new[5] = new[4] + new[3]
        l.append(new)
    new1 = node.copy()
    if new1[1] >= 2:
        new1[1] -= 2
        new1[2] = new1[0] + new1[1]
        new1[4] += 2
        new1[5] = new1[4] + new1[3]
        l.append(new1)
    new2 = node.copy()
    if new2[1] >= 1 & new2[0] >= 1:
        new2[0] -= 1
        new2[1] -= 1
        new2[2] = new2[0] + new2[1]
        new2[3] += 1
        new2[4] += 1
        new2[5] = new2[3] + new2[4]
        l.append(new2)
    print(l)


no = [3, 3, 6, 0, 0, 0]
lista = [no]
print(lista)
part(lista[0], lista)
