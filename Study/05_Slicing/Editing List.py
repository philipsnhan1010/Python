# list of Andy's dozen favourite films (give or take)
films = (
    "Cabaret", "The Matrix", "The Parent Trap", "The Sound of Music",
    "Laa Laa land", "The Prestige", "Love Actually", "Raiders of the Lost Ark",
    "12 Angry Men", "Die Hard", "A Few Good Men", "Casablanca"
)
# Convert films from tulpe to list
films_list = list(films)

# Edit list
films_list[4] = "La La Land"

# Remove the last 3 films in the list
films_list[-3:] = []

# Create a new list: two best and worst films
best_and_worst = films_list[:2] + films_list[-2:]

print(films_list)
print(best_and_worst)