
# Go to a website and return results
import requests

response = requests.get("https://www.google.com")
print(response.text)