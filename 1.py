
def task_1():
    from math import ceil

    length = 11
    # Длина
    k = 3
    # Мощность алфавита
    # 3 бита на символ
    # 2^3 = 8

    password = ceil(11 * 3 / 8) # округляем вверх

    count = 20

    return password * count


def task_2():
    # идентификатор объекта, описание структуры объекта и дополнительную информацию
    from math import ceil

    obj_id = ceil(7 * 5 / 8)
    # 22 буквы
    # для этого нужно 5 бит
    # 2^5=32
    # округляем в большую сторону

    obj_structure = ceil(70 * 11 / 8)
    # 1789
    # для этого нужно 11 бит
    # 2^11 = 2048
    # округляем в большую сторону

    obj = 2 * 1024 * 1024 / 16384

    return int(obj - obj_id - obj_structure)


def task_3():
    from math import ceil
    # код сотрудника, код подразделения и некоторая дополнительная информация

    sot_code = ceil(18 * 5 / 8) # 2^5=32 > 30
    sot_pod = ceil(10 / 8) # 2^10=1024 > 1000
    sot = 30
    sot_dop = sot - sot_code - sot_pod

    return int(sot_dop)


def task_4():
    from math import ceil

    obj_id = ceil(105 * 11 / 8) # 2^11=2048 > 1510

    mass = obj_id * 16384 / 1024

    return int(mass)


def task_5():
    from math import ceil

    password = ceil(16 * 3 / 8) # 2^3=8 > 7

    mass = password * 30

    return int(mass)


def task_6():
    # A  B  C  D  E  F
    # 10 11 12 13 14 15
    for x in range(0, 10):
        x1 = x * 17 ** 3 +\
            11 * 17 ** 2 +\
             0 * 17 ** 1 +\
             9 * 17 ** 0

        x2 = x * 15 ** 3 +\
             8 * 15 ** 2 +\
            14 * 15 ** 1 +\
             8 * 15 ** 0
        r = x1 + x2
        if r % 155 == 0:
            return r // 155


def task_7():
    # A  B  C  D  E  F
    # 10 11 12 13 14 15
    # yAAx + x02y

    lst = []

    for x in range(0, 12):
        for y in range(0, 12):
            x1 = y * 12 ** 3 +\
                10 * 12 ** 2 +\
                10 * 12 ** 1 +\
                 x * 12 ** 0

            x2 = x * 14 ** 3 +\
                 0 * 14 ** 2 +\
                 2 * 14 ** 1 +\
                 y * 14 ** 0
            lst.append(x1 + x2)

    lst = [r for r in lst if r % 80 == 0]
    return min(lst) // 80


def task_8():
    # A  B  C  D  E  F
    # 10 11 12 13 14 15
    # yAAx + x02y

    lst = []

    for x in range(0, 10):
        x1 = 3 * 14 ** 3 +\
             x * 14 ** 2 +\
            13 * 14 ** 1 +\
            10 * 14 ** 0

        x2 = 5 * 12 ** 3 +\
             x * 12 ** 2 +\
            10 * 12 ** 1 +\
             6 * 12 ** 0
        r = x1 + x2
        if r % 81 == 0:
            return r // 81


def task_9():
    # A  B  C  D  E  F
    # 10 11 12 13 14 15
    # yAAx + x02y

    lst = []

    for x in range(0, 9):
        for y in range(0, 9):
            x1 = 8 * 9 ** 4 +\
                 8 * 9 ** 3 +\
                 x * 9 ** 2 +\
                 4 * 9 ** 1 +\
                 y * 9 ** 0

            x2 = 7 * 11 ** 3 +\
                 x * 11 ** 3 +\
                 4 * 11 ** 2 +\
                 4 * 11 ** 1 +\
                 y * 11 ** 0
            lst.append(x1 + x2)

    lst = [r for r in lst if r % 61 == 0]
    return min(lst) // 61


def task_10():
    # A  B  C  D  E  F
    # 10 11 12 13 14 15
    # yAAx + x02y

    lst = []

    for x in range(0, 10):
        x1 = 4 * 15 ** 3 +\
            12 * 15 ** 2 +\
             x * 15 ** 1 +\
             4 * 15 ** 0

        x2 = x * 13 ** 3 +\
             6 * 13 ** 2 +\
             2 * 13 ** 1 +\
            10 * 13 ** 0
        lst.append(x1 + x2)

    lst = [r for r in lst if r % 121 == 0]
    return min(lst) // 121


def task_11():
    def f(n):
        s = bin(n)[2:]
        s = s + str(s.count("1") % 2)
        s = s + str(s.count("1") % 2)
        return int(s, 2)        

    for i in range(200):
        r = f(i)
        if r > 93:
            return r
            break


def task_12():
    def f(n):
        n = str(n)
        x1 = str(int(n[0]) + int(n[1]))
        x2 = str(int(n[1]) + int(n[2]))
        return x1 + x2

    count = 0
    for i in range(100, 999 + 1):
        if f(i) == "1715":
            count += 1
    return count


def task_13():

    def f(n):
        return n ^ ((1 << 8) - 1)
        # s = bin(n)[2:].zfill(8)
        # s = ''.join(['0' if x == '1' else '1' for x in s])
        # return s
    
    for i in range(128, 256):
        # print(bin(i)[2:], bin(f(i))[2:].zfill(8))
        if i - f(i) == 105:
            return i


def task_14():
    raise NotImplementedError("task_14 not implemented")


def task_15():
    raise NotImplementedError("task_15 not implemented")


def task_16():
    raise NotImplementedError("task_16 not implemented")


def task_17():
    raise NotImplementedError("task_17 not implemented")


def task_18():
    raise NotImplementedError("task_18 not implemented")


def task_19():
    raise NotImplementedError("task_19 not implemented")


def task_20():
    raise NotImplementedError("task_20 not implemented")


def task_21():
    raise NotImplementedError("task_21 not implemented")


def task_22():
    raise NotImplementedError("task_22 not implemented")


def task_23():
    raise NotImplementedError("task_23 not implemented")


def task_24():
    raise NotImplementedError("task_24 not implemented")


def task_25():
    raise NotImplementedError("task_25 not implemented")


def task_26():
    raise NotImplementedError("task_26 not implemented")


def task_27():
    raise NotImplementedError("task_27 not implemented")


def task_28():
    raise NotImplementedError("task_28 not implemented")


def task_29():
    raise NotImplementedError("task_29 not implemented")


def task_30():
    raise NotImplementedError("task_30 not implemented")


def task_31():
    raise NotImplementedError("task_31 not implemented")


def task_32():
    raise NotImplementedError("task_32 not implemented")


def task_33():
    raise NotImplementedError("task_33 not implemented")


def task_34():
    raise NotImplementedError("task_34 not implemented")


def task_35():
    raise NotImplementedError("task_35 not implemented")


def task_36():
    raise NotImplementedError("task_36 not implemented")


def task_37():
    raise NotImplementedError("task_37 not implemented")


def task_38():
    raise NotImplementedError("task_38 not implemented")


def task_39():
    raise NotImplementedError("task_39 not implemented")


def task_40():
    raise NotImplementedError("task_40 not implemented")


import os

if os.name == 'nt':
    exec('import os; os.system("cls")')
else:
    exec('import os; os.system("clear")')


for i in range(1, 40 + 1):
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
