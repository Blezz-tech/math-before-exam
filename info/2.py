
def task_1():
    from math import ceil
    x = 113
    k = 11 # 2048 > 2025

    t = x * k / 8
    t = ceil(t)

    return t * 32768 / 1024


def task_2():
    #  A  B  C  D  E  F
    # 10 11 12 13 14 15

    for x in range(0, 46 + 1):
        x1 = 1 * 47 ** 4 +\
             x * 47 ** 3 +\
             2 * 47 ** 2 +\
             4 * 47 ** 1 +\
            10 * 47 ** 0

        x2 = x * 47 ** 4 +\
             2 * 47 ** 3 +\
             0 * 47 ** 2 +\
             2 * 47 ** 1 +\
             4 * 47 ** 0

        x3 = 6 * 47 ** 3 +\
             x * 47 ** 2 +\
             0 * 47 ** 1 +\
             8 * 47 ** 0
        
        r = x1 + x2 - x3
        if r % 46 == 0:
            return r


def task_3():
    def f(x):
        s = bin(x)[2:]

        if s.count("1") > s.count("0"):
            s = s + '1'
        else:
            s = s + '0'

        return int(s, 2)

    for i in range(300):
        r = f(i)
        if r > 80:
            return r


def task_4():
    def f(n):
        if n <= 2:
            return 2
        return f(n - 1) + 2 * f(n - 2)

    return f(5)


def task_5():
    from itertools import product

    count = 0
    for s in product("ТИМОФЕЙ", repeat=5):
        s = "".join(list(s))
        v0 = s.count("Й") <= 1 and s[0] != 'Й' and s[-1] != 'Й'
        v1 = ("ЙИ" not in s) and ("ИЙ" not in s)

        if v0 and v1:
            count += 1
    
    return count


def task_6():
    def convert(x):
        s = ''

        while x:
            s = s + str(x % 9)
            x //= 9
        
        return s[::-1]

    lst = []
    for A in range(1000):
        x = convert(729 ** 105 - 3 ** 56 + A)

        if str(x).count("8") == 290:
            lst.append(A)

    return min(lst)


def task_7():
    for A in range(0, 300):
        if all([
            (2*x + 3*y < A) or (x >= y) or (y > 24)
            for x in range(0, 100)
            for y in range(0, 100)
        ]):
            return A


def task_8():
    def f(x, y):
        if x > y or x == 13:
            return 0
        elif x == y:
            return 1
        else:
            return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)

    return f(3, 8) * f(8, 18)


def task_9():
    max_sum_of_digit = 0
    max_number = 0
    for x1 in range(1000, 3162):
        # 2 3
        # 7 8
        if str(x1)[-1] not in '27':
            continue
        x2 = x1 + 1
        r = x1 * x2
        r_sum_of_digit = sum([int(x) for x in str(r)])
        if r_sum_of_digit >= max_sum_of_digit:
            max_number = r
            max_sum_of_digit = r_sum_of_digit
    
    return max_number


def task_10():
    raise NotImplementedError("task_10 not implemented")   


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
