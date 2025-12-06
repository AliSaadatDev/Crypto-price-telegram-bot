import requests

api_key = "" # Get api key from https://fast-creat.ir or @Api_ManagerRoBot in telegram (api_key is free for Nobitex data)
id = "raven"

class ChartCrypto:
    def __init__(self, api_key, id):
        self.api_key = api_key
        self.id = id
        self.base_url = "https://api.fast-creat.ir/chart"

    def get_chart(self, symbol):
        symbol = symbol.upper()
        url = f"{self.base_url}?apikey={self.api_key}&symbol={symbol}&id={self.id}&type=1"
        response = requests.get(url)
        data = response.json()
        return data['result']

