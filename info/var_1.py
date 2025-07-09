def task_9():
    def f(x):
        return sum(map(int, str(x)))

    max_sum = 0
    max_x = 0
    for x1 in range(3164, 1001, -1):
        if str(x1)[-1] not in "1368":
            continue
        x2 = x1 + 1
        r = x1 * x2

        max_sum_curr = f(r)
        if max_sum_curr > max_sum:
            max_sum = max_sum_curr
            max_x = r
    
    print(max_x)

    # 12
    # 34
    # 67
    # 89
    # 1001  3162


task_9()

def task_10():
    def f1():
        count = 0
        for x5 in range(2): 
            for x6 in range(2): 
                for x7 in range(2): 
                    for x8 in range(2):
                        if (x5 == x6) and (x7 <= x8):
                            count += 1
        return count / (2 ** 4)

    def f2():
        count = 0
        for x9 in range(2): 
            for x10 in range(2): 
                for x11 in range(2): 
                    for x12 in range(2):
                        if (x9 == x10) and (x11 <= x12) and (x9 == x12):
                            count += 1
        return count / (2 ** 4)

    def f3():
        count = 0
        for x13 in range(2): 
            for x14 in range(2): 
                for x15 in range(2): 
                    for x16 in range(2):
                        if (x13 == x14) and (x15 <= x16) and (x13 == x16):
                            count += 1
        return count / (2 ** 4)

    def f4():
        count = 0
        for x1 in range(2): 
            for x2 in range(2): 
                for x3 in range(2): 
                    for x4 in range(2):
                        for x17 in range(2):
                            for x18 in range(2):
                                for x19 in range(2):
                                    for x20 in range(2):
                                        v0 = (x1 == x2) and (x3 <= x4)
                                        v1 = x1 == x17
                                        v2 = (x17 == x18) and (x19 <= x20) and (x17 == x20)
                                        if v0 and v1 and v2:
                                            count += 1
        return count / (2 ** 8)

    count = (2 ** 20) * f1() * f2() * f3() * f4()

    print(count)