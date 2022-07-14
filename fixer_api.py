from credentials import *

class FixerApi:
	API_URL = "https://api.apilayer.com/fixer/"
	
	def __init__(self):
		self.headers = { "apikey": credentials['fixerApiKey'] }
	
	def convert_params(self, input_currency, output_currency, amount):
		return {
			"data": { },
			"headers": self.headers,
			"method": "GET",
			"url": f"{self.API_URL}convert?to={output_currency}&from={input_currency}&amount={amount}"
		}
