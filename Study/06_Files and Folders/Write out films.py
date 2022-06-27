bad_list = ["Titanic", "Home Alone"]

with open(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\bad_list.txt","w") as bad_movies:
    #title
    bad_movies.write("Lap's Bad films list\n")
    bad_movies.writelines("\n".join(bad_list))

print("DONE!")
