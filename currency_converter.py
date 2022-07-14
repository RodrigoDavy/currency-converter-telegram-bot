from fixer_api import FixerApi
from requests import request

class CurrencyConverter:
    def __init__(self, api = FixerApi()):
        self.api = api
    
    def convert(self, input_currency, output_currency, amount):
        params = self.api.convert_params(input_currency, output_currency, amount)
        return self.__make_request(params)
        
    def __make_request(self, params):
        return request(params['method'], params['url'], headers = params['headers'], data = params['data'])
