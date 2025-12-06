import requests

api_key = "" # Get api key from https://fast-creat.ir or @Api_ManagerRoBot in telegram (api_key is free for Nobitex data)
url = f"https://api.fast-creat.ir/nobitex/v2?apikey={api_key}"

class GetAllDataNobitex:
    def __init__(self):
        self.url = url

    def get_coins(self):
        response = requests.get(self.url)
        data = response.json()
        return data["result"]

    def get_price(self, symbol):
        symbol = symbol.upper()
        coins = self.get_coins()

        if symbol not in coins:
            return None
        
        coin = coins[symbol]

        return {
            "name": coin["name"],
            "IRR": coin["irr"],
            "USDT": coin["usdt"],
            "dayChange": coin["dayChange"]
        }
