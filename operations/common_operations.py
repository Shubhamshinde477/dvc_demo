import os


def get_dataset_path(file_name: str):
    ROOT_DIR = os.path.abspath(os.curdir)
    file = os.path.join(ROOT_DIR,"datasets",file_name)
    return file