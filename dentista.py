def build(index, left, right, base, i_tree, p_tree):
    if right - left < 2:
        #print(base[left])
        i_tree[index] = base[left] % 2
        p_tree[index] = 1 - (base[left] % 2)
    else:
        middle = int((right + left) / 2)
        build(index * 2, left, middle, base, i_tree, p_tree)
        build(index * 2 + 1, middle, right, base, i_tree, p_tree)
        i_tree[index] = i_tree[index * 2] + i_tree[index * 2 + 1]
        p_tree[index] = p_tree[index * 2] + p_tree[index * 2 + 1]


def summ(l, r, inicio, fim, indice, tree):
    if l >= fim or r <= inicio:
        return 0
    if l <= inicio and r >= fim:
        return tree[indice]
    mid = int((inicio + fim) / 2)
    return summ(l, r, inicio, mid, indice * 2, tree) + summ(l, r, mid, fim, indice * 2 + 1, tree)


def modify(pos, value, ind, begin, end, tree_i, tree_p, v):
    #print(ind, pos, begin, end)
    tree_i[ind] += (value % 2) - (v[pos] % 2)
    tree_p[ind] += (1 - value % 2) - (1 - v[pos] % 2)
    m = int((begin + end) / 2)
    if (end - begin) < 2:
        tree_i[ind] = value % 2
        tree_p[ind] = 1 - value % 2
        v[pos] = value
    elif pos < m:
        modify(pos, value, ind * 2, begin, m, tree_i, tree_p, v)
    else:
        modify(pos, value, ind * 2 + 1, m, end, tree_i, tree_p, v)


size = int(input())
a = input().split()
a = list(map(int, a))
a = [0] + a
#print(a)
requisition = int(input())
b = [0] * requisition
i = 0
odd = [0] * (4 * size)
par = [0] * (4 * size)
build(1, 1, size+1, a, odd, par)
#print(odd)
#print(par)
#print(summ(1, size+1, 1, size+1, 1, odd))
for i in range(0, requisition):
    b[i] = list(map(int, input().split()))
for i in range(0, requisition):
    if b[i][0] == 0:
        modify(b[i][1], b[i][2], 1, 1, size+1, odd, par, a)
    elif b[i][0] == 1:
        print(summ(b[i][1], b[i][2] + 1, 1, size + 1, 1, par))
    else:
        print(summ(b[i][1], b[i][2] + 1, 1, size + 1, 1, odd))
#print(b)
