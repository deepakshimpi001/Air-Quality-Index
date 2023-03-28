import os


try:
    directory="Data"
    current_dir=os.getcwd()
    path=os.path.join(current_dir,directory)
    os.mkdir(path)
except FileExistsError:
    print('folder Already Created')
except Exception as e:
    print(e)
else:
    print('ab kya krna hai')
finally:
    print("ye to hoga hi")