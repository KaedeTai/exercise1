
from random import randint
from random import random
from datetime import datetime
from datetime import timedelta

symbols = ['BTC', 'ETH']
eotts = ['GDAX', 'BTSP', 'BTCX', 'POLO', 'FLYR', 'ETHF']

for i in range(1000):
    sn = '%03i' % i
    f = open('data/data%s.txt' % sn, 'w')
    time = datetime(2017, 6, 1)
    stop = datetime.now()
    while True:
        minutes = randint(0, 59)
        seconds = randint(0, 59)
        microseconds = randint(0, 999999)
        time += timedelta(0, seconds, microseconds, 0, minutes)
        if time > stop: break
        symbol = symbols[randint(0, 1)]
        price = (7129.29 if symbol == 'BTC' else 810.42) * (random() * 0.2 + 0.9) #+-10%
        qty = randint(-300, 300)
        eott = eotts[randint(0, len(eotts)-1)]
        f.write('%s %s %.2f %i %s\n' % (time.strftime('%Y%m%d %H:%M:%S:%f'), symbol, price, qty, eott))
    f.close()

