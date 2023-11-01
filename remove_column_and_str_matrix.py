
# удаления строки и столбца из исходной матрицы
def remove_row_column():
    pass

# вычисление определителя матрицы
def calculate_determinant():
    pass

# вывод матрицы на экран
def print_matrix():
    pass

# Подменю ввода матрицы
def sub_switch(option):
    if option == '1':
        # Ввод данных вручную
        matrix = []
        print("Данные введены вручную")
        return matrix

    elif option == '2':
        # Генерация случайной матрицы
        matrix = []
        print("Данные сгенерированы")
        return matrix

    elif option == '3':
        # Выход в главное меню
        pass
    else:
        print("\nНекорректный выбор")


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
                matrix = sub_switch(sub_menu_option)

        elif option == '2':
            if matrix is not None:
                # Ввод номера строки и столбца для удаления
                while True:
                    row_number = int(input("Введите номер строки для удаления: "))
                    column_number = int(input("Введите номер столбца для удаления: "))
                    break
                matrix = []
                matrix_point = True
                determinant = 0
                console = input("Нажмите Enter, чтобы продолжить")
            else:
                print("\nИсходные данные не введены")

        elif option == '3':
            if matrix is not None and matrix_point == True:
                print("\nМатрица без удаленной строки и столбца:")
                print_matrix()
                print("Определитель матрицы:")
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