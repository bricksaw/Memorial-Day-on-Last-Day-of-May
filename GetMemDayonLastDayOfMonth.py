import datetime

y = 1950
while (y < 2050):   
  d = datetime.datetime(y,5,31)
  if d.strftime("%w") == "1":
    print(d)
  y = y + 1
