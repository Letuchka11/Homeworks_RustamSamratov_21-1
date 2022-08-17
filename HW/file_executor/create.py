import os
from pathlib import Path

def create_file(file_name ,extension):
    if os.path.isfile(f'{file_name}{extension}'):
        print("такой файл уже есть")
    else:
        myFile = open(f'{file_name}{extension}', "w")
        myFile.close()
        print(Path(f"{file_name}{extension}").absolute())
        print("Ваш файл создам")


