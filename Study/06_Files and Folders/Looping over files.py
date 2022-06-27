import glob

files = glob.glob(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\\*.py",recursive=True)
files_1 = glob.glob(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\\**\*.py",recursive=True)
for file in files:
    print(file)