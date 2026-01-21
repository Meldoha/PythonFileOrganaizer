import os
import shutil


def main():
    f_path = os.path.join(input('Путь к папке: '))
    going_to_a_folder(f_path)
    sorting() 



##Переходим к папке
def going_to_a_folder(f_name):
    try:
        os.chdir(f_name)
    except FileNotFoundError:
        print("Папка не найдена")
        exit()



##Создаём папку
def create_folder(folder_name):
    try:
        os.mkdir(folder_name)
    except FileExistsError:
        pass


##Сортируем
def sorting():

    for item in os.listdir():

        if '.' not in item:
            continue

        cor_path = os.path.join(os.getcwd(), item)

        if os.path.isfile(cor_path):
            ext = item.split('.')[-1]
            create_folder(ext)

            new_name = f'{ext} - {item}'
            path = os.path.join(ext, new_name)

            shutil.move(item, path)
            


if __name__ == "__main__":
    main()