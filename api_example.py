from credentials import *
import requests

input_currency = 'CLP'
output_currency = 'BRL'
amount = 1000

url = f"https://api.apilayer.com/fixer/convert?to={output_currency}&from={input_currency}&amount={amount}"

payload = {}
headers= {
  "apikey": credentials['fixerApiKey']
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
print(result)
