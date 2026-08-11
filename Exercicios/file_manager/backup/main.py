import os
import shutil

PATH = os.path.dirname(os.path.abspath(__file__))
PATHcwd = os.path.join(os.getcwd(), 'Exercicios', 'file_manager')
PATHbackup = os.path.join(os.getcwd(), 'Exercicios', 'file_manager', 'backup')


def show_direct(path):
    for root, _, files in path:
        print(f"{os.path.basename(root)}/")

        for file in files:
            print(f"  {file}")

def filesizes(path):
    for root, _, files in os.walk(path):
        for file in files:
            path = os.path.join(root, file)

            sizeinbytes = os.path.getsize(path)
            sizeinmegas = sizeinbytes / (1024 * 1024)
            print(f'Name file: {file}\n Size: {sizeinmegas:.2f}MB\n')

def renamefiles():
    oldname = input('Actual file name: ')
    newname = input('New file name: \n')

    for root, dirs, files in os.walk(PATH):
        if 'backup' in dirs:
            dirs.remove('backup')
        for file in files:
            if file == oldname:
                oldpath = os.path.join(root, file)
                newpath = os.path.join(root, newname)
                os.rename(oldpath, newpath)
                print('\nSucessfully renamed!\n')
                return
    print('\nFile not found!\n')

def movefile():
    filename = input('Name file: ')
    newpath = input('New file folder: ')
    for root, dirs, files in os.walk(PATH):
        if 'backup' in dirs:
            dirs.remove('backup')
        for file in files:
            if file == filename:
                oldpath = os.path.join(root, file)
                newpath = os.path.join(PATH, newpath)
                shutil.move(oldpath, newpath)
                return
    print('\nFile not found!\n')

while True:
    print('==== FILE MANAGER ====')
    print('\n1 - Show directory tree')
    print('2 - Show file sizes')
    print('3 - Create backup')
    print('4 - Rename file')
    print('5 - Move file')
    print('6 - Delete backup')
    print('0 - Exit')
    choice = input('Choice a option: ')

    if choice == '1':
        show_direct(os.walk(PATH))
    elif choice == '2': 
        filesizes(PATHcwd)
    elif choice == '3':
        shutil.copytree(PATH, PATHbackup)
    elif choice == '4':
        renamefiles()
    elif choice == '5':
        movefile()
    elif choice == '6':
        try:
            shutil.rmtree(PATHbackup)
        except FileNotFoundError:
           print('Backup not found! ')
    elif choice == '0':
        print('Closing program...')
        break
    else:
        print('Invalid option!')