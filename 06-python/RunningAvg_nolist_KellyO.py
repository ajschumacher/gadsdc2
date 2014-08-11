import math

l = 1
m = 0
while True:
    n = raw_input("Please enter a number:")
    if n.strip() == 'done':
        break
    n = int(n)
    m += n
    fl = float(m)
    print (fl/l)
    l += 1
