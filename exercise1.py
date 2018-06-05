from glob import glob
from math import fabs

sum = 0
count = 0
abs = 0

for file in glob('data/*'):
    for line in open(file):
        (date, time, symbol, price, qty, eott) = line.strip().split(' ')
        price = float(price)
        qty = int(qty)

        if date < '20170601' or date > '20180201': continue
        if time < '10:00:00.000000' or time > '11:59:59.999999': continue

        sum += price * qty
        count += qty
        abs += fabs(price * qty)

print(sum, count, abs)