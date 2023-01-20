import os
import tests.resources


def generate_path_upload(name_file):
    return os.path.abspath(os.path.join(os.path.dirname(tests.resources.__file__), name_file))