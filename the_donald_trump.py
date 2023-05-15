import requests

request = "https://www.tronalddump.io/random/quote"
response = requests.get(request).json()
quote = response['value']
print(f'\n\n{quote}\n\n')
