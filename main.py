import os
import shutil


def main():
    print("Путь к папке: ", end="")
    f_path = os.path.join(input())
    going_to_a_folder(f_path)
    sorting()


def going_to_a_folder(f_name):

    try:
        os.chdir(f_name)
        print(f"Вы в папке: {os.getcwd()}")
    except FileNotFoundError:
        print("Папка не найдена")


def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
        print(f'Создана папка с именем "{folder_name}". Путь: {os.getcwd()}')
    except FileExistsError:
        print("Папка с таким именем уже существует!")


def sorting():
    all_files = os.listdir()

    for item in all_files:

        cor_path = os.path.join(os.getcwd(), item)

        if os.path.isfile(cor_path):
            try:
                create_folder(item.split('.')[-1])
                os.rename(item, os.path.join(item.split('.')[-1], item))
            except:
                print('Папка уже существует')


main()