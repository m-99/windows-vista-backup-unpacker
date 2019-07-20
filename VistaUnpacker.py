import os
import zipfile
import shutil

def unzip(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if file.endswith('.zip'):
                with zipfile.ZipFile(os.path.join(rootdir, file)) as zip_ref:
                    zip_ref.extractall(rootdir)

def consolidate(rootdir):
    for subdir, dirs, files in os.walk(rootdir):
        for file in files:
            if (not file.endswith('.zip')) and (file != __file__):
                filepath = os.path.join(subdir, file)
                new_filepath = path_without_immediate_parent(filepath, rootdir)
                os.makedirs(os.path.dirname(new_filepath), exist_ok=True)
                shutil.move(filepath, new_filepath)

def without_rootdir(filepath, rootdir):
    return filepath[len(rootdir)+1:]

def without_parent_directory(filepath):
    directory_end = filepath.index('\\')
    return filepath[directory_end+1:]

def path_without_immediate_parent(filepath, rootdir):
    return os.path.join(rootdir, without_parent_directory(without_rootdir(filepath, rootdir)))


if __name__ == '__main__':
    realpath = os.path.realpath(__file__)
    rootdir, _ = os.path.split(realpath)
    unzip(rootdir)
    consolidate(rootdir)
