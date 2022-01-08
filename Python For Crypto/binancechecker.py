# binancechecker.py
from binance import Client
import time

api_key = 'BjBsuqEEcrHYTgRNpeQ18JdEFZUYVjAkk0js6qKMcoY88YwcNC7gK7ooNL2psP50'
api_secret = 'T13AnYAbcK60EGp5GTcDd86z624XqD5I86Wm0PDmO6L5jRe7NtddD19O4KD7qRtn'
client = Client(api_key, api_secret)

#depth = client.get_order_book(symbol='BTCBUSD')
#print(depth)


mycoin = ['BTCBUSD','SLPUSDT','ETHUSDT']
mycoin = ['BTCBUSD']

while True:
    prices = client.get_all_tickers()
    for p in prices:
        for c in mycoin:
            sym = c
            if p['symbol'] == sym:
                pc = float(p['price'])#ราคาบิทคอยหน่อย usd
                rate = 32.26
                cal = pc * rate
                print('เหรียญ: {} ราคา: {:,.3f} บาท'.format(sym,cal))
                print('ราคา USD: {}'.format(pc))
                print('--------')
    time.sleep(0.5)
