# ШАГ. Д/з по сроку 29/06/2023 © Заливко Денис

import func230629 as hw
import std_func as myf

print(
"""
Д/з по сроку 29/06/2023:

1) 12.5.б. Дан двумерный массив. Вывести на экран:
    б) все элементы s-го столбца массива.

2) 12.6.б. Дан двумерный массив. Вывести на экран:
    б) все элементы m-й строки массива.

3) 12.16.а. Составить программу:
    а) расчета разности двух любых элементов двумерного массива.

4) 12.33.а. Дан двумерный массив. Вывести на экран:
    а) все элементы пятого столбца массива, начиная с последнего элемента этого столбца.

5) 12.62.а. Дан двумерный массив. Найти:
    а) сумму элементов каждой строки.

6) 12.90.а.б. (двумя способами - не нужно) Дан двумерный массив. В каждой его строке найти:
    а) максимальный элемент;
    б) минимальный элемент.

""")

taskNumber = int(input('\nВведите номер запускаемой задачи: '))

matrix = myf.initial_int_matrix(6)
myf.fill_int_matrix_random(matrix)
print('Матрица:')
myf.print_matrix(matrix)

if 1 < taskNumber > 6:
        print('Ошибка! Значение введено неверно!')
elif taskNumber == 1:
    hw.f_12_5_b(matrix)

elif taskNumber == 2:
    hw.f_12_6_b(matrix)

elif taskNumber == 3:
    res_1216a = hw.f_12_16_a(matrix)
    print()
    print(f'array[{res_1216a[3][0]}][{res_1216a[3][1]}] = {res_1216a[1]}')
    print(f'array[{res_1216a[3][2]}][{res_1216a[3][3]}] = {res_1216a[2]}')
    print(f'Разница между элементами: {res_1216a[0]}')

elif taskNumber == 4:
    res_1233a = hw.f_12_33_a(matrix)
    myf.print_vector(res_1233a)

elif taskNumber == 5:
    res_1262a = hw.f_12_62_a(matrix)
    myf.print_vector(res_1262a)

elif taskNumber == 6:
    res_1290ab = hw.f_12_90_a_b(matrix)
    print('\nМаксимальные значения в каждой строке:')
    myf.print_vector(res_1290ab[0])
    print('\n\nМинимальные значения в каждой строке:')
    myf.print_vector(res_1290ab[1])
    print()


