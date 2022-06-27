import glob

# Create variables to hold the list of files
files = glob.glob(r"G:\SelfStudy\python\Practice\Study\06_Files and Folders\\**\*.csv", recursive=True)
# print(files)

# Sort them into file name order 
files.sort(key= lambda x:x.rpartition("\\")[-1])

# Print a title for the output
print("Number".center(20) + "Country".center(60) + "Area".rjust(20))

# Loop over the files
for file in files:
    # Open file for reading
    with open(file) as this_file:
        # Get and print the file name for debugging purpose
        #print(file)
        file_path, test, file_name = file.rpartition("\\")
        #print(file_path, file_name)
        # Get all but the first line
        lines = this_file.read().splitlines()[1:]
        #print(lines)
        # Loop over lines
        for line in lines:
            number, country, area = line.split(",")
            print(str(number).center(20) + country.center(60) + area.rjust(20))