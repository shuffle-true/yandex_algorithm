# Юра решил подготовиться к собесу Яшки. Выбрал на литкоде N задач. В первый день Юрец решил К задач,
# а в каждый след день Юра решал на одну задачу больше чем в предыдущий.

# Определите, сколько дней уйдет у Юры на подготовку к собесу.

# Будем искать минимальное кол-во дней, достаточное для решения N задач.
#
#     K ...... K + 1 ........... K + M - 1
#    M - общее число задач, которые он решил

def lbinsearch(l, r, check, params):
    while l < r:
        m = (l + r) // 2
        if check(m, params):
            r = m
        else:
            l = m + 1
    return l


def checktask(m, params):
    n, k = params
    return ((2 * k + m - 1) * m / 2) >= n

if __name__ == '__main__':
    n, k = 50, 1
    params = (n, k)
    print(lbinsearch(0, n, checktask, params))