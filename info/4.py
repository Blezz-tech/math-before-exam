
def task_1():
    # личный код, номер и дополнительная информация

    from math import ceil

    code = ceil(15 * 5 / 8) # 32 > 20 + 9
    nom = ceil(7 / 8) # 128 > 80

    dop = 20 - code - nom

    return dop


def task_2():
    for x in range(10):
        #  A  B  C  D  E  F
        # 10 11 12 13 14 15

        x1 = x * 13 ** 3 +\
            10 * 13 ** 2 +\
             0 * 13 ** 1 +\
             4 * 13 ** 0

        x2 = 1 * 18 ** 3 +\
            13 * 18 ** 2 +\
             x * 18 ** 1 +\
             3 * 18 ** 0
        
        r = x1 + x2
        if r % 184 == 0:
            return r // 184


def task_3():
    raise NotImplementedError("task_3 not implemented")


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
