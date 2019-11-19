import os
import shutil
import datetime
import zipfile


def unzip_single(src_file, dest_dir):
    ''' 解压单个文件到目标文件夹。
    '''
    zf = zipfile.ZipFile(src_file)
    try:
        zf.extractall(path=dest_dir)
    except RuntimeError as e:
        print(e)
    zf.close()


def main():
    for zip_file_name in os.listdir(PATH_INPUT):
        if zip_file_name[-3:] != 'zip':
            continue
        path_zip_file = os.path.join(PATH_INPUT, zip_file_name)
        print('正在解压： ', path_zip_file)
        unzip_single(src_file=path_zip_file, dest_dir=PATH_OUTPUT)


if __name__ == '__main__':
    PATH_ROOT = os.path.dirname(__file__)
    PATH_CONFIG = os.path.join(PATH_ROOT, '0.Configuration')
    PATH_INPUT = os.path.join(PATH_ROOT, '1.Output_ZipFile')
    PATH_OUTPUT = os.path.join(PATH_ROOT, '2.Output_SimulationPnlFiles')

    if os.path.exists(PATH_OUTPUT):
        shutil.rmtree(PATH_OUTPUT)
    os.mkdir(PATH_OUTPUT)

    main()

    # os.system('pause')
