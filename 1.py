
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
