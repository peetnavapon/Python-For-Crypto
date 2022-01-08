#testline.py

from songline import Sendline
token = 'your token'
messenger = Sendline(token)

#messenger.sendtext('สวัสดีจ้าาา')

messenger.sticker(3,1,'บิทคอยราคาต่ำแล้ว')

messenger.sendimage('https://cf.shopee.co.th/file/5160e1eb7f9b68c33e15e06780dac2ca')
