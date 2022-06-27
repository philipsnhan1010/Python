
# films = open(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\films.txt","r")
# # lines = films.readlines()
# # lines = films.read(40)
# # lines = films.readline()
# for line in films:
#     bits = line.split(" - ")
#     #print(bits)
#     film_number, film_name = bits
#     print(film_number, film_name.strip())

# films.close()

# Using WITH
with open(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\films.txt","r") as movie_list:
    for line in movie_list:
        bits = line.split(" - ")
        films_number, film_name = bits
        print(films_number, film_name.strip())
    