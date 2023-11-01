
def remove_row_column(matrix, row, column):
    return matrix

def calculate_determinant(matrix):
    return matrix

def print_matrix(matrix):
    # Вывод матрицы
    for row in matrix:
        print(' '.join([str(element) for element in row]))

def sub_switch(option, matrix, size):
    if option == '1':
        # Ввод данных вручную
        matrix = []
        for i in range(size):
            row = input(f"Введите элементы {i + 1}-й строки через пробел:").split()
            matrix.append([int(element) for element in row])
        return matrix

    elif option == '2':
        # Генерация случайной матрицы
        matrix = []
        return matrix

    elif option == '3':
        return matrix
    else:
        print("\nНекорректный выбор")
        return matrix

def main():
    matrix = None
    matrix_point = False

    while True:
        print("\nВыберите действие:")
        print("1. Ввести исходные данные")
        print("2. Выполнить алгоритм")
        print("3. Вывести результат")
        print("4. Завершить работу программы")
        option = str(input("Введите число от 1 до 4: "))

        if option == '1':
            sub_menu_option = '0'
            while sub_menu_option != '3':
                print("\nВыберите действие:")
                print("1. Ввести данные вручную")
                print("2. Сгенерировать случайным образом")
                print("3. Вернуться в меню")
                sub_menu_option = str(input("Введите число от 1 до 3: "))
                size = int(input("Введите размер квадратной матрицы: "))
                matrix = sub_switch(sub_menu_option, matrix, size)

        elif option == '2':
            if matrix is not None:
                # Ввод номера строки и столбца для удаления
                while True:
                    try:
                        # Удаление строки и столбца
                        row_number = int(input("Введите номер строки для удаления: "))
                        column_number = int(input("Введите номер столбца для удаления: "))
                        break
                    except ValueError as a:
                        # Если введён некорректный символ
                        print("Введён неккоректный символ, повтори попытку!")
                matrix = remove_row_column(matrix, row_number - 1, column_number - 1)
                matrix_point = True
                # Вычисление определителя
                determinant = calculate_determinant(matrix)
                console = input("Нажмите Enter, чтобы продолжить")
            else:
                print("\nИсходные данные не введены")

        elif option == '3':
            if matrix is not None and matrix_point == True:
                # Вывод результата
                print("\nМатрица без удаленной строки и столбца:")
                print_matrix(matrix)
                print("Определитель матрицы:", int(determinant))
                matrix_point = False
                console = input("Нажмите Enter, чтобы продолжить")
            else:
                print("\nИсходные данные не введены или не отработал алгоритм")

        elif option == '4':
            console = input("Нажмите Enter!")
            break

        else:
            print("\nНекорректный выбор. Пожалуйста, повторите попытку!")

if __name__ == "__main__":
    main()