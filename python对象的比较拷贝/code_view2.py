import copy

if __name__ == "__main__":
    # 深拷贝
    l1 = [[1, 2], (30, 40)]
    l2 = copy.deepcopy(l1)
    l1.append(100)
    l1[0].append(3)

    print("l1 = ", l1)
    print("l2 = ", l2)

    x = [1]
    x.append(x)
    print(x)

    y = copy.deepcopy(x)
    print(y)

    print(x==y)
