def write_file(file_path, data):
    with open(file_path, "w") as file:
        file.write(data)

def append_file(file_path, data):
    with open(file_path, "a") as file:
        file.write(data)


import os
def rename_file(old_name, new_name):
    os.rename(old_name, new_name)