import requests
import zipfile
import hashlib
import shutil
import os

def download_file(url, file_path):
    # Скачиваем архив по ссылке
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)

def extract_archive(archive_path, extract_path):
    # Распаковываем архив
    with zipfile.ZipFile(archive_path, 'r') as archive:
        archive.extractall(extract_path)

def calculate_checksum(file_path):
    # Вычисляем MD5 хэш-сумму содержимого файла
    with open(file_path, 'rb') as file:
        contents = file.read()
        checksum = hashlib.md5(contents).hexdigest()
    return checksum

def overwrite_file(source_path, destination_path):
    # Копируем содержимое исходного файла в целевой файл
    shutil.copyfile(source_path, destination_path)

def calculate_checksum_for_folder(folder_path):
    # Контрольная сумма
    checksums = {}
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            checksum = calculate_checksum(file_path)
            checksums[file_path] = checksum
    return checksums

def create_archive(archive_path, folder_path):
    # Создаем архив
    with zipfile.ZipFile(archive_path, 'w') as archive:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                archive.write(file_path, os.path.relpath(file_path, folder_path))

def pack_archive(file_paths, archive_name):
    # Упаковываем архив
    with zipfile.ZipFile(archive_name, "w") as zip_ref:
        for file_path in file_paths:
            zip_ref.write(file_path)