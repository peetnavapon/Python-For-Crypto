# bitkubchecker.py

import requests
from pprint import pprint
import time


API_HOST = 'https://api.bitkub.com'

mycoin = ['THB_BTC','THB_ETH','THB_DOGE']

while True:
    response = requests.get(API_HOST + '/api/market/ticker')
    result = response.json()

    #pprint(result['THB_BTC'])
    for c in mycoin:
        #sym = 'THB_BTC'
        sym = c 
        data = result[sym]
        last = data['last']
        #print(data)
        print(sym, last)
    print('-----')
    time.sleep(0.5)


#########GUI###################



    from tkinter import *
    from tkinter import ttk

    GUI = Tk()
    GUI.geometry('500x600')
    GUI.title('เช็คราคาจาก Bitkub')

    FONT1 = ('Angsana New',30)

    L1 = ttk.Label(text='ราคา bitkub ล่าสุด',font=FONT1)
    L1.pack()

    #B1 = ttk.Button(GUI,text='Check',command=CheckPrice)
    #B1.pack(ipadx=20 , ipady=10)


    v_result = StringVar()
    v_result.set ('---------result-----------')


    R1 = ttk.Label(textvariable=v_result,font=FONT1)
    R1.pack()

    #Run ฟังชันทุกครั้งที่เปิด
    GUI.mainloop()

