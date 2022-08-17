import os

def write_to_file(file, body):
    if os.path.isfile(file):
        with open(file , "w") as filee:
            filee.write(body)
            filee.close()
    else:
        print("Нет файла")

