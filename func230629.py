import std_func as myf

"""
12.5.б. Дан двумерный массив. Вывести на экран:
    б) все элементы s-го столбца массива.

12.6.б. Дан двумерный массив. Вывести на экран:
    б) все элементы m-й строки массива.

12.16.а. Составить программу:
    а) расчета разности двух любых элементов двумерного массива.

12.33.а. Дан двумерный массив. Вывести на экран:
    а) все элементы пятого столбца массива, начиная с последнего элемента этого столбца.

12.62.а. Дан двумерный массив. Найти:
    а) сумму элементов каждой строки.

12.90.а.б. (двумя способами - не нужно) Дан двумерный массив. В каждой его строке найти:
    а) максимальный элемент;
    б) минимальный элемент.

"""


def f_12_5_b(matrix: list[[int]]):
    """
    12.5.б. Дан двумерный массив. Вывести на экран:
        б) все элементы s-го столбца массива.
    :return: None. Выводит на экран.
    """
    s = myf.answer_rnd_int_number(0, len(matrix[0]))
    print(f'Столбец для вывода на печать: {s}')
    axis_y = myf.get_matrix_axis_y(matrix, s-1)
    for index in range(0, len(axis_y)):
        print(f'array[{index}, {s}] = {axis_y[index]}')
    return None


def f_12_6_b(matrix: list[[]]):
    """
    12.6.б. Дан двумерный массив. Вывести на экран:
        б) все элементы m-й строки массива.
    :return: None. Выводит на экран.
    """
    m = myf.answer_rnd_int_number(0, len(matrix))
    print(f'Строка для вывода на печать: {m}')
    axis_x = myf.get_matrix_axis_x(matrix, m-1)
    for index in range(0, len(axis_x)):
        print(f'array[{m}, {index}] = {axis_x[index]}')
    return None


def f_12_16_a(matrix: list[[int]]) -> tuple:
    """
    12.16.а. Составить программу:
        а) расчета разности двух любых элементов двумерного массива.
    :returns:
        matrix[m][n] - matrix[m1][n1] (0)
        matrix[m][n] (1), matrix[m1][n1] (2)
        (3)
        (m:int (0), n:int (1),
        m1:int (2), n1:int (3))

    """
    m = myf.answer_rnd_int_number(0, len(matrix)-1)
    n = myf.answer_rnd_int_number(0, len(matrix[0])-1)

    m1 = myf.answer_rnd_int_number(0, len(matrix)-1)
    n1 = myf.answer_rnd_int_number(0, len(matrix[0])-1)

    return \
        matrix[m][n] - matrix[m1][n1], \
            matrix[m][n], matrix[m1][n1], \
            (m, n, m1, n1)


def f_12_33_a(matrix: list[[]]) -> tuple:
    """
    12.33.а. Дан двумерный массив. Вывести на экран:
        а) все элементы пятого столбца массива, начиная с последнего элемента этого столбца.
    :return: Вектор (кортеж с соответствующими значениями)
    """
    return tuple(myf.get_vector_reverse(list(myf.get_matrix_axis_y(matrix, 5-1))))


def f_12_62_a(matrix: list[[int]]) -> tuple:
    """
    12.62.а. Дан двумерный массив. Найти:
        а) сумму элементов каждой строки.
    :return: Кортеж со значениями суммы элементов соответствующей строки матрицы
    """
    return tuple(sum(matrix[i]) for i in range(0, len(matrix)))


def f_12_90_a_b(matrix: list[[]]) -> tuple:
    """
    12.90.а.б. (двумя способами - не нужно) Дан двумерный массив. В каждой его строке найти:
        а) максимальный элемент;
        б) минимальный элемент.
    :return:
    """
    return tuple(max(matrix[index]) for index in range(0, len(matrix))), \
        tuple(min(matrix[index]) for index in range(0, len(matrix)))
