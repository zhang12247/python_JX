def generator(k):
    i = 1
    while True:
        yield i ** k
        i += 1


def get_sum(n):
    sum_1, sum_3 = 0, 0
    for i in range(n):
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print("next_1 = {}，next_3 = {}".format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
        print("sum_1 = {}，sum_3 = {}".format(sum_1, sum_3))
    print(sum_1 * sum_1, sum_3)


if __name__ == "__main__":
    gen_1 = generator(1)
    gen_3 = generator(3)
    print(gen_1)
    print(gen_3)
    get_sum(8)

