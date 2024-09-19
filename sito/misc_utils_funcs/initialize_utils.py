import os


def init_directory(directory_path):
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)


def init_file(file_path):
    if not os.path.exists(file_path):
        open(file_path, "w").close()