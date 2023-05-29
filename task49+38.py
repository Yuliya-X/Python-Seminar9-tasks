# Задача 49: Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.

# Подзадачи: вывод вариантов использования проги (меню)
# 1. запись данных в формате .txt
# 2. информация должна хранить: фамилию, имя, номер тел, описание (0-3)
# 3. вывод данных
# 4. поиск по значению: фамилия [0], номер [2]
# 5. внести нового абонента
# 6. удалить запись по фамилии
# 7. выйти из меню


# НЕ РАБОТАЕТ! РАЗОБРАТЬ ПОЧЕМУ НЕ РАБОТАЕТ! читает файлы
# ISO-8859-1 - работал, но не читал, utf-8 - ругался на кодировку,
# заработало после изменения кодировки файла в командах и сохранение


# читает файлы
def read_csv(filename: str) -> list:
    phonebook = []
    contact = ["Фамилия", "Имя", "Номер телефона", "Описание"]
    with open(filename, 'r', encoding='utf-8') as data:
        for line in data:
            contact = line.strip().split(',')
            phonebook.append(contact)
    return phonebook

# import csv
# читает файлы с помощью import csv
# def read_csv(filename: str) -> list:
#     with open("phonebook.csv", 'r', newline="") as file:
#         reader = csv.reader(file)
#         phonebook = list(reader)
#     return phonebook


# пишет в файлы
def write_csv(filename: str) -> list:
    with open(filename, 'w', encoding='utf-8') as f:
        for contact in phonebook:
            f.write(
                f"{contact[0]}, {contact[1]}, {contact[2]}\n")


# пишет в файлы
def save_to_txt(phonebook):
    with open('phones.txt', 'w', encoding='utf-8') as f:
        for contact in phonebook:
            f.write(f"{contact[0]}, {contact[1]}, {contact[2]}\n")
    print("Справочник успешно сохранен в файл phones.txt")


# пользовательский интерфейс
def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Удалить абонента по фамилии\n"
          "7. Закончить работу")
    return int(input())


# показать содержимое справочника
def show_phonebook(phonebook):
    # печать с отступами
    print(f"{'Фамилия':10} {'Имя':10} {'Номер телефона':15}")
    # печать разделительной полосы в размер отспупов
    print(f"{'-'*10} {'-'*10} {'-'*15}")
    for contact in phonebook:
        print(f"{contact[0]:10} {contact[1]:10} {contact[2]:15}\n")


# поиск абонета по фамилии
def find_by_last_name(phonebook):
    last_name = input("Введите фамилию: ")
    for contact in phonebook:
        if contact[0] == last_name:
            return print(f"{contact[0]}, {contact[1]}, {contact[2]}")
    else:
        print("Абонент с такой фамилией не найден")


# поиск абонента по номеру телефона
def find_by_phone_number(phonebook):
    phone_number = input("Введите номер телефона: ")
    for contact in phonebook:
        if contact[2] == phone_number:
            return print(f"{contact[0]}, {contact[1]}, {contact[2]}")
    else:
        print("Абонент с таким номером телефона не найден")


# добавляет нового абонента в справочник
def add_contact(phonebook: list):
    last_name = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    phone_number = input("Введите номер телефона: ")
    phonebook.append([last_name, first_name, phone_number])
    print("Абонент успешно добавлен в справочник")
    return phonebook


# удаляет абонента из справочника по фамилии
def remove_by_last_name(phonebook):
    last_name = input("Введите фамилию для удаления: ")
    for contact in phonebook:
        if contact[0] == last_name:
            phonebook.remove(contact)
            return print(f"Абонент с фамилией {last_name} удален из справочника")
    else:
        print("Абонент с такой фамилией не найден в справочнике")


# работа по сценарию
def workWithPhonebook():
    while True:
        choice = show_menu()
        if choice == 1:
            show_phonebook(phonebook)
        elif choice == 2:
            find_by_last_name(phonebook)
        elif choice == 3:
            find_by_phone_number(phonebook)
        elif choice == 4:
            add_contact(phonebook)
            write_csv("phonebook.csv")
        elif choice == 5:
            save_to_txt(phonebook)
        elif choice == 6:
            remove_by_last_name(phonebook)
            write_csv("phonebook.csv")
        elif choice == 7:
            print("Работа программы завершена")
            break
        else:
            print("Некорректный ввод. Попробуйте еще раз")


filename = "phonebook.csv"
phonebook = read_csv(filename)
workWithPhonebook()
