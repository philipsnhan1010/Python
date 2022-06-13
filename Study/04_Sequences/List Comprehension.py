## 1: List even square

    # Basic way
# for num in range(1,21):
#     if num % 2 == 0:
#         print(num ** 2)

    # List comprehension way
# numbers = [x ** 2 for x in range(1,21) if x % 2 == 0]
# for num in numbers:
#     print(num)

## 2: List "l" letter in quote
    # Steve Job's quote
# quote = "Your time is limited, so don't waste it living someone else's life. Don't be trapped by dogma – which is living with the results of other people's thinking"
# words = quote.split()
    # Without comprehension
# for word in words:
#     if "l" in word.lower():
#         print(word[::-1])

    # With comprehension
# backward_words = [word[::-1] for word in words if "l" in word.lower()]
# for w in backward_words:
#     print(w)

## 3 - List hyperlink
import requests
response = requests.get("https://webscraper.io/test-sites/")

if response.status_code != 200:
    print("URL not found")
    exit()

lines = response.text.splitlines()

    # Without comprehension
# for line in lines:
#     if "<a" in line:
#         print(line.strip())

    # Version 2
hyper_links = [line.strip() for line in lines if "<a" in line]
for l in hyper_links:
    print(l)