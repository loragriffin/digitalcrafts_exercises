lista = [1, 3, 1, 5, 7, 5, 1, 3, 5, 6, 2]


def repeat_num(x):
    sorted_list = sorted(lista)
    for i in sorted_list:
        if i == sorted_list[i + 1]:
            print(i)


repeat_num(lista)
