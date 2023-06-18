import os

def list_directory(dir_name):
    return os.listdir(dir_name)

def list_files(dir_path):
    files = []
    for file in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, file)):
            files.append(file)
    return files