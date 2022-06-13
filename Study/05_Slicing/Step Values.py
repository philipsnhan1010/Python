# the first 20 numbers
integers = range(1,21)

# list of Andy's dozen favourite films (give or take)
films = (
    "Cabaret", "The Matrix", "The Parent Trap", "The Sound of Music",
    "Laa Laa land", "The Prestige", "Love Actually", "Raiders of the Lost Ark",
    "12 Angry Men", "Die Hard", "A Few Good Men", "Casablanca"
)

# String containing quotation from Martin Niemoller (a German Lutheran pastor)
quote = "First they came for the socialists, and I did not speak out — because I was not a socialist. Then they came for the trade unionists, and I did not speak out — because I was not a trade unionist. Then they came for the Jews, and I did not speak out — because I was not a Jew. Then they came for me — and there was no one left to speak for me."

# Print even numbers
# for num in integers[1::2]:
#     print(num)

# Print out every fifth film
#print(films[::5])

# quote backward
sample_string = quote[:10]
print(sample_string[-1::-1])

# "socialists" in reverse order
print(quote.split()[5][-2::-1])