
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
    min_x = min(lst) / 80
    return int(min_x)


def task_8():
    raise NotImplementedError("task_8 not implemented")


def task_9():
    raise NotImplementedError("task_9 not implemented")


def task_10():
    raise NotImplementedError("task_10 not implemented")


def task_11():
    raise NotImplementedError("task_11 not implemented")


def task_12():
    raise NotImplementedError("task_12 not implemented")


def task_13():
    raise NotImplementedError("task_13 not implemented")


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
