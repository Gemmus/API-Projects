import requests

url = "https://cat-fact.herokuapp.com/facts"
response = requests.get(url).json()
fact = response[0]['text']
print(f'\n\n{fact}\n\n')