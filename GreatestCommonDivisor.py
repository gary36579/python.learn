# Greatest Common Divisor, GCD


# Euclidean algorithm
def GreatestCommonDivisor1(x, y):
    return y if x % y == 0 else GreatestCommonDivisor1(y, x % y)


# Short division
def GreatestCommonDivisor2(x, y):
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

    return result



if __name__ == '__main__':
    greatestCommonDivisor1 = GreatestCommonDivisor1(40, 64)
    greatestCommonDivisor2 = GreatestCommonDivisor1(12, 72)
    greatestCommonDivisor3 = GreatestCommonDivisor1(24, 60)
    greatestCommonDivisor4 = GreatestCommonDivisor1(28, 68)
    greatestCommonDivisor5 = GreatestCommonDivisor1(13, 17)
    greatestCommonDivisor6 = GreatestCommonDivisor2(40, 64)
    greatestCommonDivisor7 = GreatestCommonDivisor2(12, 72)
    greatestCommonDivisor8 = GreatestCommonDivisor2(24, 60)
    greatestCommonDivisor9 = GreatestCommonDivisor2(28, 68)
    greatestCommonDivisor10 = GreatestCommonDivisor2(13, 17)
    greatestCommonDivisor11 = GreatestCommonDivisor2(1, 17)

    # print(greatestCommonDivisor1)
    # print(greatestCommonDivisor2)
    # print(greatestCommonDivisor3)
    # print(greatestCommonDivisor4)
    # print(greatestCommonDivisor5)
    # print(greatestCommonDivisor6)
    # print(greatestCommonDivisor7)
    # print(greatestCommonDivisor8)
    # print(greatestCommonDivisor9)
    # print(greatestCommonDivisor10)
    # print(greatestCommonDivisor11)

    assert greatestCommonDivisor1 == 8
    assert greatestCommonDivisor2 == 12
    assert greatestCommonDivisor3 == 12
    assert greatestCommonDivisor4 == 4
    assert greatestCommonDivisor5 == 1
    assert greatestCommonDivisor6 == 8
    assert greatestCommonDivisor7 == 12
    assert greatestCommonDivisor8 == 12
    assert greatestCommonDivisor9 == 4
    assert greatestCommonDivisor10 == 1
    assert greatestCommonDivisor11 == 1
