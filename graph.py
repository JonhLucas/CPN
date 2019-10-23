def ida(node, l1, l2):
    x = (node[1] > node[0] & node[0] == 0)
    y = (node[1] <= node[0])
    x = x or y
    a = (node[4] > node[3] & node[3] == 0)
    b = (node[4] <= node[3])
    a = a or b
    c = node not in l1
    print(x and a, l1[0] != node, node not in l2,"ida: ", node)
    if x and a:
        new = node.copy()
        if new[0] >= 2:
            new[0] -= 2
            new[2] = new[0] + new[1]
            new[3] += 2
            new[5] = new[4] + new[3]
            if new not in l1:
                lista.append(new)
                l1.append(new)
                print("inserido", new)
                volta(new, l1, l2)
        new = node.copy()
        if new[1] >= 2:
            new[1] -= 2
            new[2] = new[0] + new[1]
            new[4] += 2
            new[5] = new[4] + new[3]
            if new not in l1:
                lista.append(new)
                l1.append(new)
                print("inserido", new)
                #print(new)
                volta(new, l1, l2)
        new = node.copy()
        if new[1] >= 1 & new[0] >= 1:
            new[0] -= 1
            new[1] -= 1
            new[2] = new[0] + new[1]
            new[3] += 1
            new[4] += 1
            new[5] = new[3] + new[4]
            if new not in l1:
                lista.append(new)
                l1.append(new)
                print("inserido", new)
                #print(new)
                volta(new, l1, l2)
        new = node.copy()
        if new[0] >= 1:
            new[0] -= 1
            new[2] = new[0] + new[1]
            new[3] += 1
            new[5] = new[4] + new[3]
            if new not in l1:
                lista.append(new)
                l1.append(new)
                print("inserido", new)
                #print(new)
                volta(new, l1, l2)
        new = node.copy()
        if new[1] >= 1:
            new[1] -= 1
            new[2] = new[0] + new[1]
            new[4] += 1
            new[5] = new[4] + new[3]
            if new not in l1:
                lista.append(new)
                l1.append(new)
                print("inserido", new)
                #print(new)
                volta(new, l1, l2)
    else:
        print("recusado ida: ", node)

def volta(no, l1, l2):
    x =(no[4] > no[3] & no[3] == 0)
    y = (no[4] <= no[3])
    x = x or y
    a = (no[1] > no[0] & no[0] == 0)
    b = (no[1] <= no[0])
    a = a or b
    print(x and a, "volta: ", no)
    if x and a:
        new_node = no.copy()
        if new_node[3] >= 1:
            new_node[3] -= 1
            new_node[5] -= 1
            new_node[0] += 1
            new_node[2] += 1
            if new_node not in l2:
                lista.append(new_node)
                l2.append(new_node)
                print("--- ",new_node)
                ida(new_node, l1, l2)
        new_node = no.copy()
        if new_node[3] >= 2:
            new_node[3] -= 2
            new_node[5] -= 2
            new_node[0] += 2
            new_node[2] += 2
            if new_node not in l2:
                lista.append(new_node)
                l2.append(new_node)
                print("--- ",new_node)
                ida(new_node, l1, l2)
        new_node = no.copy()
        if new_node[4] >= 1:
            new_node[4] -= 1
            new_node[5] -= 1
            new_node[1] += 1
            new_node[2] += 1
            if new_node not in l2:
                lista.append(new_node)
                l2.append(new_node)
                print("--- ",new_node)
                ida(new_node, l1, l2)
        new_node = no.copy()
        if new_node[4] >= 2:
            new_node[4] -= 2
            new_node[5] -= 2
            new_node[1] += 2
            new_node[2] += 2
            if new_node not in l2:
                lista.append(new_node)
                l2.append(new_node)
                print("--- ",new_node)
                ida(new_node, l1, l2)
        new_node = no.copy()
        if new_node[3] >= 1 & new_node[4] >= 1:
            new_node[3] -= 1
            new_node[4] -= 1
            new_node[5] -= 2
            new_node[0] += 1
            new_node[1] += 1
            new_node[2] += 2
            if new_node not in l2:
                lista.append(new_node)
                l2.append(new_node)
                print("--- ", new_node)
                ida(new_node, l1, l2)
            else:
                print("erro")
        print("fim")
    else:
        print("recusado volta: ", no)


no = [3, 3, 6, 0, 0, 0]
lista = [no]
l1 = [no]
l2 = []
ida(lista[0], l1, l2)
print(lista)
print(l1)
print(l2)
