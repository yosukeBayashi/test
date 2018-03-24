import requests
from pprint import pprint

#r = requests.get('https://api.bitflyer.jp/v1/board?product_code=BTC_JPY')
r = requests.get('https://api.bitflyer.jp/v1/board?product_code=FX_BTC_JPY')

json = r.json()
asks = json["asks"]
asks_1 = asks[0:20]
#asks_2 = asks_1.reverse()
#print(type(asks))
pprint(asks_1[::-1])

print("-------------------")
print(json["mid_price"])
print("-------------------")

bids = json["bids"]
bids_1 = bids[0:20]
pprint(bids_1)
# #pprint(json)


