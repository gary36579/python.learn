from GreatestCommonDivisor import GreatestCommonDivisor1 as GCD


# Formula
def LeastCommonMultiple1(x, y):
    return (x * y) / GCD(x, y)


# Short division
def LeastCommonMultiple2(x, y):
    result = 1
    i = 1
    while i <= x and i <= y:
        if x % i == 0 and y % i == 0:
            result *= i
            x = x / i
            y = y / i
            if i == 1:
                i += 1
        else:
            i += 1

    return result * x * y


if __name__ == '__main__':
    leastCommonMultiple1 = LeastCommonMultiple2(40, 64)
    leastCommonMultiple2 = LeastCommonMultiple2(12, 72)
    leastCommonMultiple3 = LeastCommonMultiple2(24, 60)
    leastCommonMultiple4 = LeastCommonMultiple2(28, 68)
    leastCommonMultiple5 = LeastCommonMultiple2(13, 17)
    leastCommonMultiple6 = LeastCommonMultiple2(40, 64)
    leastCommonMultiple7 = LeastCommonMultiple2(12, 72)
    leastCommonMultiple8 = LeastCommonMultiple2(24, 60)
    leastCommonMultiple9 = LeastCommonMultiple2(28, 68)
    leastCommonMultiple10 = LeastCommonMultiple2(13, 17)
    leastCommonMultiple11 = LeastCommonMultiple2(1, 17)

    # print(leastCommonMultiple1)
    # print(leastCommonMultiple2)
    # print(leastCommonMultiple3)
    # print(leastCommonMultiple4)
    # print(leastCommonMultiple5)
    # print(leastCommonMultiple6)
    # print(leastCommonMultiple7)
    # print(leastCommonMultiple8)
    # print(leastCommonMultiple9)
    # print(leastCommonMultiple10)
    # print(leastCommonMultiple11)

    assert leastCommonMultiple1 == 320
    assert leastCommonMultiple2 == 72
    assert leastCommonMultiple3 == 120
    assert leastCommonMultiple4 == 476
    assert leastCommonMultiple5 == 221
    assert leastCommonMultiple6 == 320
    assert leastCommonMultiple7 == 72
    assert leastCommonMultiple8 == 120
    assert leastCommonMultiple9 == 476
    assert leastCommonMultiple10 == 221
    assert leastCommonMultiple11 == 17
