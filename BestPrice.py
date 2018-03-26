import requests

def bitflyer():
    URL = 'https://lightning.bitflyer.jp/v1/getticker'
    ticker = requests.get(URL).json() 
    price = int(ticker['best_ask']),int(ticker['best_bid'])
    return price
    
def coincheck():
    URL = 'https://coincheck.com/api/ticker'
    ticker = requests.get(URL).json() 
    price = int(ticker['ask']),int(ticker['bid'])
    return price

def zaif():
    url = 'https://api.zaif.jp/api/1/ticker/btc_jpy'
    ticker = requests.get(url).json()
    price = int(ticker['ask']),int(ticker['bid'])
    return price
    
def btcbox():
    url = 'https://www.btcbox.co.jp/api/v1/ticker'
    ticker = requests.get(url).json()
    price = int(ticker['buy']),int(ticker['sell'])
    return price

def bitbank():
    URL = 'https://public.bitbank.cc/btc_jpy/ticker'
    ticker = requests.get(URL).json()['data']
    price = int(ticker['buy']),int(ticker['sell'])
    return price

def kraken():
    url = 'https://api.kraken.com/0/public/Ticker?pair=XXBTZJPY'
    ticker = requests.get(url).json()['result']['XXBTZJPY']
    price = int(float(ticker['a'][0])),int(float(ticker['b'][0]))
    return price

def quoinex():
    url = 'https://api.quoine.com/products/5'
    ticker = requests.get(url).json()
    price = int(ticker['market_ask']),int(ticker['market_bid'])
    return price

def fisco():
    url = 'https://api.fcce.jp/api/1/ticker/btc_jpy'
    ticker = requests.get(url).json()
    price = int(ticker['ask']),int(ticker['bid'])
    return price

x = [bitflyer(),coincheck(),zaif(),btcbox(),bitbank(),kraken(),quoinex(),fisco()]
store = ['bitflyer','coincheck','zaif','btcbox','bitbank','kraken','quoinex','fisco']

ask = []
bid = []

for i in x:
    ask.append(i[0])
    bid.append(i[1])


dic = {}
count = 0
for i in store:
    dic.update({ask[count]:i})
    count += 1
ask_num = sorted(ask)[0]
best_ask = dic[ask_num]


dic = {}
count = 0
for i in store:
    dic.update({bid[count]:i})
    count += 1
bid_num = sorted(bid,reverse=True)[0]
best_bid = dic[bid_num]


print(best_ask + ' で買い ' + best_bid + ' で売ると ' + str("¥{:,d}".format(bid_num - ask_num)) + ' の利益')
