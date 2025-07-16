
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
            return x


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
