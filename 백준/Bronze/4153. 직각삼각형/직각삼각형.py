while 1:
    # (1)
    a, b, c = map(int, input().split())

    # (2)
    if a == 0 and b == 0 and c == 0:
        break

    # (3)
    list_value = []

    # (4)
    list_value.append(a)
    list_value.append(b)
    list_value.append(c)

    # (5)
    list_value = sorted(list_value)

    # (6)
    pow_1 = pow(list_value[0], 2)
    pow_2 = pow(list_value[1], 2)
    pow_3 = pow(list_value[2], 2)

    # (7)
    if pow_3 == pow_1 + pow_2:
        print("right")

    else:
        print("wrong")