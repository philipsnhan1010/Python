import glob

files = glob.glob(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\\**\*.txt",recursive=True)
for file in files:
    print(file)