# create a tuple to hold male name
male_friends = ("Tom","Jerry","Andy")
print(male_friends)
print(type(male_friends))

# create a list to hole female name
female_friends = ["Rebecca","Phoebe","Marria"]
print(female_friends)
print(type(female_friends))

# Tuple is Immutable which mean it does not allow to change its elements
#male_friends[1] = "Hardy"
#print(male_friends)

# List is Mutable which mean it allow to change elements
female_friends[0] = "Julia"
print(female_friends)

# Convert Tuple to List
new_male_friends = list(male_friends)
new_male_friends[0] = "Rey"
print(new_male_friends)

# Range
even_numbers = range(2, 10, 2)
print(type(even_numbers))
print(even_numbers[3])

# String
lap_nhan = "Nhan Minh Lap"
print(type(lap_nhan))
print(lap_nhan[2])

# Only list is mutable, Tuple, Range and String are Immutable