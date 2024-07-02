import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from get_rates import GetRates
import pygame

pygame.init()

INTERVAL = 500
TICK_AMT = 1000

sound_on = True

fig = plt.figure(figsize=(12, 6))

plt.axis([0, 1000, 1.087, 1.09])

ask_price1 = 0
ask_price2 = 0
bid_price1 = 0
bid_price2 = 0

last_ask1 = 0
last_ask2 = 0
last_bid1 = 0
last_bid2 = 0

x_ask1 = [.0]
y_ask1 = [.0]
x_ask2 = [.0]
y_ask2 = [.0]
x_bid1 = [.0]
y_bid1 = [.0]
x_bid2 = [.0]
y_bid2 = [.0]

xt1 = 0
yt1 = .0

xt2 = 0
yt2 = .0

ask_list1 = []
ask_list2 = []
bid_list1 = []
bid_list2 = []

ln_ask1, = plt.plot(x_ask1, y_ask1, '-', color ='green')
ln_ask2, = plt.plot(x_ask2, y_ask2, '-', color ='blue')
ln_bid1, = plt.plot(x_bid1, y_bid1, '-', color ='green')
ln_bid2, = plt.plot(x_bid2, y_bid2, '-', color ='blue')


ask1txt = plt.text(.1, .1, '', fontsize=10)
ask2txt = plt.text(.1, .2, '', fontsize=10)
bid1txt = plt.text(.1, .1, '', fontsize=10)
bid2txt = plt.text(.1, .2, '', fontsize=10)

cortxt1 = plt.text(xt1, yt1, '', fontsize=14)
cortxt2 = plt.text(xt2, yt2, '', fontsize=14)

def ask1func(frames):

    global ask_price1

    rates = GetRates()

    ask1 = rates.get_rates('EURUSD').ask

    askflt = float(ask1)
    ask_price1 = askflt
    ask_list1.append(askflt)

    ask1txt.set_text(f'EURUSD ask: {ask_price1}')
    return ask1txt

def bid1func(frames):

    global bid_price1

    rates = GetRates()

    bid1 = rates.get_rates('EURUSD').bid

    bidflt1 = float(bid1)
    bid_price1 = bidflt1
    bid_list1.append(bidflt1)

    bid1txt.set_text(f'EURUSD bid: {bid_price1}')
    return bid1txt

def ask2func(frames):

    global ask_price2

    rates = GetRates()

    ask2 = rates.get_rates('GBPUSD').ask

    askflt = float(ask2)
    ask_price2 = askflt
    ask_list2.append(askflt)

    ask2txt.set_text(f'GBPUSD ask: {ask_price2}')
    return ask2txt

def bid2func(frames):

    global bid_price2

    rates = GetRates()

    bid2 = rates.get_rates('GBPUSD').bid

    bidflt2 = float(bid2)
    bid_price2 = bidflt2
    bid_list2.append(bidflt2)

    bid2txt.set_text(f'GBPUSD bid: {bid_price2}')
    return bid2txt

def cor1(frames):

    global ask_list1
    global ask_list2
    global xt1
    global sound_on

    print(ask_list1)
    print(ask_list2)

    askcor = 0

    if len(ask_list1) >= TICK_AMT and len(ask_list2) >= TICK_AMT:
        askcor = np.corrcoef(ask_list1[-TICK_AMT:-1], ask_list2[-TICK_AMT:-1])
        askcor = askcor[0, 1]

    xt1 += 1
    cortxt1.set_x(xt1)
    cortxt1.set_y((last_ask1 + last_ask2) / 2)
    if len(ask_list1) >= TICK_AMT and len(ask_list2) >= TICK_AMT and askcor <= 0 and sound_on == True:
        pygame.mixer.music.load("WW_Get_Rupee.mp3")
        pygame.mixer.music.play()
        sound_on = False
    if len(ask_list1) >= TICK_AMT and len(ask_list2) >= TICK_AMT and askcor >= .90 and sound_on == False:
        sound_on = True
        pygame.mixer.music.load("WW_Get_Rupee.mp3")
        pygame.mixer.music.play()
    if len(ask_list1) >= TICK_AMT and len(ask_list2) >= TICK_AMT:
        cortxt1.set_text(f'{round(askcor, 2)}')
    elif len(ask_list1) <= TICK_AMT and len(ask_list2) <= TICK_AMT:
        cortxt1.set_text(f'len1 = {len(ask_list1)}\nlen2 = {len(ask_list2)}')
    return cortxt1


def cor2(frames):

    global bid_list1
    global bid_list2
    global xt2

    print(bid_list1)
    print(bid_list2)


    bidcor = 0

    if len(bid_list1) >= TICK_AMT and len(bid_list2) >= TICK_AMT:
        bidcor = np.corrcoef(bid_list1[-TICK_AMT:-1], bid_list2[-TICK_AMT:-1])
        bidcor = bidcor[0, 1]

    xt2 += 1
    cortxt2.set_x(xt2)
    cortxt2.set_y((last_bid1 + last_bid2) / 2)
    if len(bid_list1) >= TICK_AMT and len(bid_list2) >= TICK_AMT:
        cortxt2.set_text(f'{round(bidcor, 2)}')
    elif len(bid_list1) <= TICK_AMT and len(bid_list2) <= TICK_AMT:
        cortxt2.set_text(f'len1 = {len(bid_list1)}\nlen2 = {len(bid_list2)}')
    return cortxt2

def update_ask_ln1(frame):
   global last_ask1

   rates = GetRates()

   ask = rates.get_rates('EURUSD').ask

   last_ask1 = float(ask)

   x_ask1.append(x_ask1[-1] + 1)
   y_ask1.append(last_ask1)
   ln_ask1.set_data(x_ask1, y_ask1)
   return ln_ask1,

def update_bid_ln1(frame):
   global last_bid1

   rates = GetRates()

   bid = rates.get_rates('EURUSD').bid

   last_bid1 = float(bid)

   x_bid1.append(x_bid1[-1] + 1)
   y_bid1.append(last_bid1)
   ln_bid1.set_data(x_bid1, y_bid1)
   return ln_bid1,


def update_ask_ln2(frame):
   global last_ask2

   rates = GetRates()

   ask = rates.get_rates('GBPUSD').ask

   last_ask2 = float(ask) - .193

   x_ask2.append(x_ask2[-1] + 1)
   y_ask2.append(last_ask2)
   ln_ask2.set_data(x_ask2, y_ask2)
   return ln_ask2,

def update_bid_ln2(frame):
   global last_bid2

   rates = GetRates()

   bid = rates.get_rates('GBPUSD').bid

   last_bid2 = float(bid) - .193

   x_bid2.append(x_bid2[-1] + 1)
   y_bid2.append(last_bid2)
   ln_bid2.set_data(x_bid2, y_bid2)
   return ln_bid2,


animation_cor1 = FuncAnimation(fig, cor1, interval=INTERVAL)
animation_cor2 = FuncAnimation(fig, cor2, interval=INTERVAL)

animation_askln1 = FuncAnimation(fig, update_ask_ln1, interval=INTERVAL)
animation_askln2 = FuncAnimation(fig, update_ask_ln2, interval=INTERVAL)
animation_bidln1 = FuncAnimation(fig, update_bid_ln1, interval=INTERVAL)
animation_bidln2 = FuncAnimation(fig, update_bid_ln2, interval=INTERVAL)

animation_ask1 = FuncAnimation(fig, ask1func, interval=INTERVAL)
animation_ask2 = FuncAnimation(fig, ask2func, interval=INTERVAL)
animation_bid1 = FuncAnimation(fig, bid1func, interval=INTERVAL)
animation_bid2 = FuncAnimation(fig, bid2func, interval=INTERVAL)


plt.show()
