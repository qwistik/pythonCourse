# variant 3
list1 = [[1, 2, 3],
       [0, 2, 4],
       [0, 5, 0],
       [0, 2, 2]]


def count_null(lst):
    count = 0

    for j in range(len(lst[0])): # for (int j = 0; j < 3; j++)
        for i in range(len(lst)): # for (int i = 0; i < 4; i++)
            if lst[i][j] == 0:
                count += 1
                break

    print(count)

count_null(list1)





lst2 = [[1, 6, 6, 1],  # 3
        [0, 2, 4, 7],  # 1
        [0, 0, 0, 6],  # 1
        [2, 1, 2, 2]]  # 2

def in_line(list):
    a = 0
    b = -1
    for i in range(len(list)):
        m = 1
        for j in range(len(list[0]) - 1):
            if list[i][j] == list[i][j + 1]:
                m += 1
        if m > a:
            a = m
            b = i

    print(b+1)

in_line(lst2)