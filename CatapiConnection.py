import requests

url = "https://catfact.ninja/fact"
response = requests.get(url)

print("Random Cat Fact:", response.json()["fact"])
