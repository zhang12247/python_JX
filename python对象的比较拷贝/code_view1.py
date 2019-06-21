if __name__ == "__main__":
    # example1
    l1 = [1, 2, 3]
    l2 = list(l1)
    print("l1是否等于l2", l1 == l2)

    # example2
    a = 10
    b = 10
    print("a是否等于b", a == b)

    print("a的地址", id(a))
    print("b的地址", id(b))

    print("a和b的地址是否相同", a is b)

    c = 25700456456456
    d = 25700456456456
    print("c和d的地址是否相同", c is d)

    t1 = (1, 2, [3, 4])
    t2 = (1, 2, [3, 4])
    print("t1和t2是否相同", t1 == t2)
    t1[-1].append(5)
    print("t1和t2是否相同", t1 == t2)

    # 浅拷贝
    s1 = set([1, 2, 3])
    s2 = set(s1)

    print("s1是否与s2值相等", s1 == s2)
    print("s1与s2是否地址相等", s1 is s2)

    l1 = [[1, 2], (30, 40)]
    l2 = list(l1)
    l1.append(100)
    l1[0].append(3)

    print("l1 = ", l1)
    print("l2 = ", l2)

    l1[1] += (50, 60)
    print("l1 = ", l1)

    print("l2 = ", l2)

