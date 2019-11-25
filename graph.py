def validate(p):
    return (p[0] >= p[1] or (p[0] < p[1] and p[0] == 0)) and (p[2] >= p[3] or (p[2] < p[3] and p[2] == 0))


def left_to_right(place, list1, list2, index):
    local = []
    for i in range(3):
        for j in range(3 - i):
            if (i or j) and place[0] >= i and place[1] >= j:
                new_node = place.copy()
                new_node[0] -= i
                new_node[1] -= j
                new_node[2] += i
                new_node[3] += j
                if new_node not in list2 and validate(new_node) and [0, 0, 3, 3] not in list2:
                    local.append(new_node)
                    list2.append(new_node)
                    if new_node == [0, 0, 3, 3]:
                        history.append([0, 0, 3, 3, index])
    while len(local) != 0 and [0, 0, 3, 3] not in list2:
        node = local.pop(0)
        history.append(node + [index])
        right_to_left(node, list1, list2, len(history) - 1)


def right_to_left(place, li1, li2, index):
    local = []
    for i in range(3):
        for j in range(3 - i):
            if (i or j) and place[2] >= i and place[3] >= j:
                new_node = place.copy()
                new_node[0] += i
                new_node[1] += j
                new_node[2] -= i
                new_node[3] -= j
                if new_node not in li1 and validate(new_node):
                    local.append(new_node)
                    li1.append(new_node)
    while len(local) != 0 and [0, 0, 3, 3] not in li2:
        node = local.pop(0)
        history.append(node + [index])
        left_to_right(node, li1, li2, len(history) - 1)


root = [3, 3, 0, 0]
history = [root+[-1]]
l1 = [root]
l2 = []
left_to_right(root, l1, l2, 0)
begin = history[-1]
path = []
while begin[4] != -1:
    path.append(begin)
    begin = history[begin[4]]
path.append(root+[-1])
path.reverse()
print(path)
