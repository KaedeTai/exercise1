from glob import glob
from math import fabs

sum = 0
count = 0
abs = 0
out = {}

for file in glob('data/*'):
    print file
    for line in open(file):
        (date, time, symbol, price, qty, eott) = line.strip().split(' ')
        price = float(price)
        qty = int(qty)

        trade = fabs(price * qty)
        key = date + ' ' + symbol
        if key not in out:
            out[key] = 0
        if trade > out[key]:
            out[key] = trade

        print key, trade

print out