# the first 20 numbers
integers = range(1,21)

# Python numbers them as:
# 0 1 2 3 4 5 6 7 8  9 10 11 12 13 14 15 16 17 18 19

# Actual numbers are:
# 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

# list of Andy's dozen favourite films (give or take)
films = (
    "Cabaret", "The Matrix", "The Parent Trap", "The Sound of Music",
    "Laa Laa land", "The Prestige", "Love Actually", "Raiders of the Lost Ark",
    "12 Angry Men", "Die Hard", "A Few Good Men", "Casablanca"
)

# String containing quotation from Martin Niemoller (a German Lutheran pastor)
quote = "First they came for the socialists, and I did not speak out — because I was not a socialist. Then they came for the trade unionists, and I did not speak out — because I was not a trade unionist. Then they came for the Jews, and I did not speak out — because I was not a Jew. Then they came for me — and there was no one left to speak for me."

# print out first 5 number
# for num in integers[0:5]:
#     print(num)

# # print out first 4 film, Excluding the first film
# for film in films[1:5]:
#     print(film)

# last 10 words in the quote
words = quote.split()
number_words = len(words)
# for word in words[number_words - 10:number_words]:
#     print(word)

# Offsetting and default values

#print 5 last words in the quote
for word in words[-5:]:
    print(word)

#print first 6 number 
for num in integers[:6]:
    print(num)

#print all the films
for film in films[:]:
    print(film)