from binance.client import Client

api_key = "enter key here"
SECRET_KEY = " enter secret here"

client = Client(api_key,SECRET_KEY)

def get_price(tick):
	price = client.futures_symbol_ticker(symbol=tick)
	return price["price"]