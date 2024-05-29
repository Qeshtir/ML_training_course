import hashlib

def calculate_md5(file_path):
    hash_md5 = hashlib.md5()  # Создаем объект MD5
    with open(file_path, "rb") as f:  # Открываем файл в бинарном режиме
        for chunk in iter(lambda: f.read(4096), b""):  # Читаем файл по частям для экономии памяти
            hash_md5.update(chunk)  # Обновляем MD5 хеш данными из файла
    return hash_md5.hexdigest()  # Возвращаем полученный хеш в виде шестнадцатеричной строки

print(calculate_md5('image-3.jpg'))
