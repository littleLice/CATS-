# 愿你早日摆脱CATS的苦海
import zipfile
import os
import datetime
import py7zr


def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)


def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def Makezip(file_dir):
    start_dir = 'C:\\XOSCATS'
    my_zip = zipfile.ZipFile(file_dir, "w", zipfile.ZIP_DEFLATED)
    for dir_path, dirs, filenames in os.walk(start_dir):
        for filename in filenames:
            my_zip.write(os.path.join(dir_path, filename))
    my_zip.close()
    print(f'备份文件为：{file_dir}')
    print("备份成功，祝你学习进步")


def Make7z(file_dir):
    start_dir = 'C:\\XOSCATS'
    archive = py7zr.SevenZipFile(file_dir, 'w')
    for dir_path, dir_names, file_names in os.walk(start_dir):
        for filename in file_names:
            fpath = dir_path.replace(start_dir, '')
            file_path = os.path.join(dir_path, filename)
            filename = os.path.join(fpath, filename)
            archive.write(file_path, arcname=filename)
    archive.close()
    print(f'备份文件为：{file_dir}')
    print("备份成功，祝你学习进步")


def main():
    mkdir('D:\\CATS备份')
    print("默认zip格式备份，速度快，但压缩效率低，压缩文件大。\n7z备份压缩时间长，但压缩文件小。")
    a = input('(0)默认zip压缩包备份\n(1)7z模式压缩备份\n(2)备份到桌面\n')
    now_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    print(f'当前时间为：{now_time}')
    if a == '0':
        file_dir = f'D:\\CATS备份\\CATS{now_time}.zip'
        Makezip(file_dir)
    elif a == '1':
        file_dir = f'D:\\CATS备份\\CATS{now_time}.7z'
        Make7z(file_dir)
    elif a == '2':
        file_dir = f"{GetDesktopPath()}\\CATS{now_time}.zip"
        Makezip(file_dir)
    else:
        Makezip(f'D:\\CATS备份\\CATS{now_time}.zip')
    input("按Enter键以退出脚本\n")


if __name__ == '__main__':
    main()
