
def task_1():
    from math import ceil

    x = 114
    k = 11 # 2048 > 1984

    r = ceil(x * k / 8)

    return r * 32768 / 1024


def task_2():
    for x in range(19):
        x1 = 9 * 19 ** 7 +\
            8 * 19 ** 6 +\
            8 * 19 ** 5 +\
            9 * 19 ** 4 +\
            7 * 19 ** 3 +\
            x * 19 ** 2 +\
            2 * 19 ** 1 +\
            1 * 19 ** 0

        x2 = 2 * 19 ** 4 +\
            x * 19 ** 3 +\
            9 * 19 ** 2 +\
            2 * 19 ** 1 +\
            3 * 19 ** 0

        r = x1 + x2
        if r % 18 == 0:
            return r // 18


def task_3():
    def f(x):
        x = str(x)
        x1 = int(x[0]) + int(x[1])
        x2 = int(x[1]) + int(x[2])
        x3 = int(x[2]) + int(x[3])

        lst = sorted([x1, x2, x3])

        return int(str(lst[1]) + str(lst[2]))

    for i in range(1000, 9999 + 1):
        r = f(i)
        if r == 1418:
            return i


def task_4():
    def f(n):
        if n == 1:
            return 1
        if n >= 2:
            return f(n - 1) * n
        
    return f(6)


def task_5():
    def convert(x):
        s = ''

        while x:
            s += str(x % 9)
            x //= 9
        return s[::-1]

    count = 0
    for i in range(0, 1_000_000):
        r = convert(i)

        v0 = r.count('4') == 1
        v1 = (r.count('1') +\
            r.count('3') +\
            r.count('5') +\
            r.count('7') +\
            r.count('9')) == 2
        v2 = len(r) == 6

        if v0 and v1 and v2:
            count += 1

    return count


def task_6():
    def convert(x):
        s = ''

        while x:
            s += str(x % 5)
            x //= 5
        return s[::-1]

    for A in range(10000):
        r = (125**52 + 25 ** 46 - A)

        if convert(r).count('4') == 86:
            return A


def task_7():
    for A in range(15, 1, -1):
        if all([
            (x&A != 0) <=( (x&10 == 0) <= (x&3 != 0))
            for x in range(300)
        ]):
            return A


def task_8():
    def f(x, y):
        if x == y:
            return 1
        if x > y or x == 29:
            return 0
        if x < y:
            return f(x + 1, y) + f(x * 2, y) + f(x * 3, y)
    
    return f(2, 13) * f(13, 44)


def task_9():
    # 1 2
    # 3 4
    # 6 7
    # 8 9
    x_max = 0
    x_sum = 0

    for x in range(10000, 31623):
        x1 = x + 1

        if str(x)[-1] not in "1368":
            continue

        r = x * x1
        r_sum = sum([int(t) for t in str(r)])
        if r_sum >= x_sum:
            x_sum = r_sum
            x_max = r
        
    return x_max


def task_10():
    return len([
        1
        for x1 in range(2)
        for x2 in range(2)
        for x3 in range(2)
        for x4 in range(2)
        for x5 in range(2)
        for x6 in range(2)
        for x7 in range(2)
        for x8 in range(2)
        if (x1 or x2) <= (x3 == x4)
        if (x3 or x4) <= (x5 == x6)
        if (x5 or x6) <= (x7 == x8)
    ])


import os

if os.name == 'nt':
    exec('import os; os.system("cls")')
else:
    exec('import os; os.system("clear")')


for i in range(1, 10 + 1):
    func_name = f"task_{i}"
    func = globals().get(func_name)
    if func:
        try:
            result = func()
            print(f"{i}:", result)
        except NotImplementedError:
            print(f"Функция {func_name} не реализована (NotImplementedError)")
    else:
        print(f"Функция {func_name} не найдена")


# for i in range(20):
#     print(f"""
# def task_{i}():
#     raise NotImplementedError("task_{i} not implemented")
# """)
