
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
    raise NotImplementedError("task_4 not implemented")


def task_5():
    raise NotImplementedError("task_5 not implemented")


def task_6():
    raise NotImplementedError("task_6 not implemented")


def task_7():
    raise NotImplementedError("task_7 not implemented")


def task_8():
    raise NotImplementedError("task_8 not implemented")


def task_9():
    raise NotImplementedError("task_9 not implemented")


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
