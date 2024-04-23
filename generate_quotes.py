import requests
import json

response = requests.get('https://zenquotes.io/api/random')
print(response)
json_data = json.loads(response.text)
quote = json_data[0]['q'] + " -" + json_data[0]['a']
print(quote)