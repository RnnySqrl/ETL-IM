from os import path, listdir


def find_ext_file(ext:str, directory:str):
    list_files = [
        path.join(directory, file)
        for file in listdir(directory)
        if file.endswith("." + ext)
    ]
    return list_files

def basepath(directory, *path_add):
    return path.join(directory, *path_add)