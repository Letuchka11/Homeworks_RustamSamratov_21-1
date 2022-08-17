import os

def delete_file(file):
    if os.path.isfile(file):
        os.remove(file)
        print("Файл успешно удален")
    else:
        print("Файла нет")