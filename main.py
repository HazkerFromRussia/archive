import modul

# использование функций из модуля
modul.download_file("http://example.com/file.zip", "downloaded_file.zip")
modul.extract_archive("downloaded_file.zip", "extracted_folder")
modul.calculate_checksum("file.txt")
modul.overwrite_file("new_file.txt", "existing_file.txt")
modul.pack_archive(["file1.txt", "file2.txt"], "packed_archive.zip")
