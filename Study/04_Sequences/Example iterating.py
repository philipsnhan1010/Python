import os

# List files in a folder
files = os.listdir(r"G:\SelfStudy\python\Practice\Study")
for file in files:
    print(file)

# Listing words
quote = "I am really miss my family in Vietnam"
words = quote.split()
for word in words:
    print(word)

# Listing builtin modules
import sys
modules = sys.builtin_module_names
for module in modules:
    if not module.startswith("_"):
        print(module)

# Listing hyperlink
import requests
response = requests.get("https://webscraper.io/test-sites/")

if response.status_code != 200:
    print("No URL found")
    exit()

lines = response.text.splitlines()
for line in lines:
    # trim line
    trimmed_line = line.strip()
    if "<a" in trimmed_line:
        print(trimmed_line)