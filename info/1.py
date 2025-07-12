
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
        return "".join(sorted([x1 , x2])[::-1])

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
    def f(n):
        n = str(n)
        x1 = str(int(n[0]) + int(n[1]))
        x2 = str(int(n[1]) + int(n[2]))
        x3 = str(int(n[2]) + int(n[3]))
        lst = sorted([x1, x2, x3])
        lst = lst[1:]
        return ''.join(lst)
        
    for i in range(9999, 999, -1):
        r = f(i)
        if r == '1315':
            return i


def task_15():
    def f(n):
        n = str(n)
        x1 = str(int(n[0]) + int(n[1]))
        x2 = str(int(n[2]) + int(n[3]))
        lst = sorted([x1, x2])[::-1]
        return ''.join(lst)
        
    for i in range(1000, 9999 + 1):
        r = f(i)
        if r == '1311':
            return i


def task_16():
    def f(n):
        if n < 3:
            return 1
        if n > 2 and n % 2 == 1:
            return f(n - 1) + 3 * f(n - 2)
        if n > 2 and n % 2 == 0:
            return sum([f(i) for i in range(1, n)])

    # return f(28)


def task_17():
    # f(2024) - f(2022)
    # 2024 - 1 + f(2023) - f(2022)
    # 2024 - 1 + 2023 - 1 + f(2022) - f(2022)
    # 2024 - 1 + 2023 - 1
    return 2024 - 1 + 2023 - 1


def task_18():
    def f(n):
        if n == 1:
            return 1
        return n * f(n - 1)

    # return f(5)
    return 1*2*3*4*5


def task_19():
    def f(n):
        if n == 1:
            return 1
        if n % 2 == 0:
            return n + f(n - 1)
        if n > 1 and n % 2 == 1:
            return 2 * f(n - 2)
    
    return f(24)


def task_20():
    # F(2022) / F(2024)
    # 2022 * F(2023) / F(2024)
    # 2022 * 2023 * F(2024) / F(2024)
    # 2022 * 2023
    return 2022 * 2023


def task_21():
    chet_and_nechet = []
    for x1 in "02468":
        for x2 in "02468":
            chet_and_nechet.append(x1 + x2)

    for x1 in "13579":
        for x2 in "13579":
            chet_and_nechet.append(x1 + x2)

    def check(s):
        return all(map(lambda x: x not in s, chet_and_nechet))

    count = 0

    for x1 in "1234567":
        for x2 in "01234567":
            for x3 in "01234567":
                for x4 in "01234567":
                    for x5 in "01234567":
                        x = x1 + x2 + x3 + x4 + x5

                        v0 = len(set(x)) == 5
                        v1 = check(x)
                        if v0 and v1:
                            count += 1
    return count


def task_22():
    from itertools import product

    glas_and_sogl = list(product("ПРБЛ", repeat=2)) + list(product("АО", repeat=2))
    glas_and_sogl = [''.join(x) for x in glas_and_sogl]

    def check1(x):
        return all([
            x.count("П") == 1,
            x.count("А") == 3,
            x.count("Р") == 1,
            x.count("Б") == 1,
            x.count("О") == 1,
            x.count("Л") == 1,
        ])

    def check2(x):
        return all(map(lambda t: t not in x, glas_and_sogl))

    def check3(x):
        return check1(x) and check2(x)

    lst = [''.join(p) for p in product("ПРБОЛА", repeat=8)]
    lst = list(filter(check3, lst))

    return len(lst)

def task_23():
    from itertools import product
    lst = [''.join(p) for p in product("0123456789AB", repeat=5)]
    lst = [x for x in lst if x[0] != '0']
    lst = [x for x in lst if x.count("7") == 1]

    def count_9AB(lst):
        return sum(1 for d in lst if d in "9AB")

    lst = [x for x in lst if count_9AB(x) <= 3]
    return len(lst)


def task_24():
    from itertools import product
    lst = [''.join(p) for p in product("ИГОРЬ", repeat=8)]
    lst = [x for x in lst if x[0] != 'Ь' and x.count("О") and x.count("Ь")]

    return len(lst)

def task_25():
    from itertools import product
    lst = [''.join(p) for p in product("СВЕТА", repeat=5)]
    lst = [x for x in lst if x.count("С") > 0]

    return len(lst)


def task_26():
    # (¬(x ∈ А) ∧ (x ∈ Q)) → (x ∈ P)
    # (x ∈ А) or (x not ∈ Q) or (x ∈ P)
    # (62;92]
    return len(range(63, 92 + 1))


def task_27():
    # x&21074 ≠ 0 → (x&12369 = 0 → x&A ≠ 0)
    # x&21074 != 0 → (x&12369 != 0 or x&A == 0)
    # (x&21074 == 0) or (x&12369 != 0) or (x&A == 0)

    for A in range(0, 1000):
        lst = []
        for x in range(0, 700):
            lst.append(
                (x & 21074 != 0) <= ((x & 12369 == 0) <= (x & A != 0))
            )
        if all(lst):
            return A


def task_28():
    for A in range(0, 100):
        lst = []
        for x in range(0, 400):
            for y in range(0, 400):
                lst.append(
                    ((x < A) <= (x**2 < 100)) and ((y**2 <= 64) <= (y <= A))
                )
        if all(lst):
            return A


def task_29():
    def f(x, A):
        return (x % A == 0) <= ((x % 21 == 0) + (x % 35 == 0))

    for A in range(1, 300):
        if all([f(x, A) for x in range(1, 300)]):
            return A


def task_30():
    def f(x, y, A):
        return (x + 2*y < A) or (y > x) or (x > 30)

    for A in range(1, 300):
        if all([f(x, y, A) for x in range(0, 300) for y in range(0, 300)]):
            return A


def task_31():
    def f(x, y):
        if x == y:
            return 1
        elif x > y or x == 14:
            return 0
        else:
            return f(x + 1, y) + f(x + 2, y)
    
    return f(2, 9) * f(9, 18)


def task_32():
    def f(x, y):
        if x == y:
            return 1
        elif x > y or x == 11 or x == 15:
            return 0
        else:
            return f(x + 1, y) + f(x + 3, y) + f(x * 2, y)
    
    return f(2, 8) * f(8, 20)


def task_33():
    def f(x, y):
        if x == y:
            return 1
        elif x > y or x == 9 or x == 15:
            return 0
        else:
            return f(x + 1, y) + f(x + 3, y) + f(x * 3, y)
    
    return f(3, 18)


def task_34():
    def f(x, y):
        if x == y:
            return 1
        elif x < y or x == 20:
            return 0
        else:
            return f(x - 2, y) + f(x // 2, y)
 
    return f(80, 40) * f(40, 1)


def task_35():
    def f(x, y):
        if x == y:
            return 1
        elif x < y or x == 12:
            return 0
        else:
            return f(x - 3, y) + f(x // 2 if x % 2 == 0 else x - 5, y)
 
    return f(36, 3)


def task_36():
    lst = [
        1
        for x1 in range(2)
        for x2 in range(2)
        for x3 in range(2)
        for x4 in range(2)
        for x5 in range(2)
        for y1 in range(2)
        for y2 in range(2)
        for y3 in range(2)
        for y4 in range(2)
        for y5 in range(2)
        if (x1 <= x2) and (x2 <= x3) and (x3 <= x4) and (x4 <= x5)
        if (y1 <= y2) and (y2 <= y3) and (y3 <= y4) and (y4 <= y5)
        if y5 <= x5
    ]

    return len(lst)


def task_37():
    # ((x1 ≡ x2) ∧ (x3 ≡ x4)) ∨ (¬(x1 ≡ x2) ∧ ¬(x3 ≡ x4)) = 0
    # A = (x1 ≡ x2) ; B = (x3 ≡ x4)
    # (A ∧ B) ∨ (¬A ∧ ¬B) = 0
    # A ≡ B = 0
    # ¬(A ≡ B)
    # ¬((x1 ≡ x2) ≡ (x3 ≡ x4))


    lst = [
        1
        for x1 in range(2)
        for x2 in range(2)
        for x3 in range(2)
        for x4 in range(2)
        for x5 in range(2)
        for x6 in range(2)
        for x7 in range(2)
        for x8 in range(2)
        for x9 in range(2)
        for x10 in range(2)
        if not ((x1 == x2) == (x3 == x4))
        if not ((x3 == x4) == (x5 == x6))
        if not ((x5 == x6) == (x7 == x8))
        if not ((x7 == x8) == (x9 == x10))
    ]

    return len(lst)


def task_38():
    # ¬(x1 ≡ x2) ∧ ( (x1 ∧ ¬x3) ∨ (¬x1 ∧ x3) ) = 0
    # ¬(x1 ≡ x2) ∧ ¬(x1 ≡ x3) = 0
    # ¬((x1 ≡ x2) ∨ (x1 ≡ x3)) = 0

    lst = [
        1
        for x1 in range(2)
        for x2 in range(2)
        for x3 in range(2)
        for x4 in range(2)
        for x5 in range(2)
        for x6 in range(2)
        for x7 in range(2)
        for x8 in range(2)
        if not ((x1 == x2) or (x1 == x3)) == 0
        if not ((x2 == x3) or (x2 == x4)) == 0
        if not ((x3 == x4) or (x3 == x5)) == 0
        if not ((x4 == x5) or (x4 == x6)) == 0
        if not ((x5 == x6) or (x5 == x7)) == 0
        if not ((x6 == x7) or (x6 == x8)) == 0
    ]

    return len(lst)


def task_39():
    raise NotImplementedError("task_39 not implemented")


def task_40():
    raise NotImplementedError("task_40 not implemented")


import os

if os.name == 'nt':
    exec('import os; os.system("cls")')
else:
    exec('import os; os.system("clear")')


for i in range(30, 40 + 1):
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
