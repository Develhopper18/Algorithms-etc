import datetime as date

tod = date.date.today() # Today
print(tod)

my_b_day = date.date(2007,8,18) # My Birthday
print(my_b_day)

dsb = (tod - my_b_day).days #MBd - dsb
print(dsb)

tdel = date.timedelta(days=10) # Adding days
print(tod + tdel)

tdel2 = date.timedelta(days=10) # Sutracting days
print(tod - tdel2)


print(tod.month) #Month
print(tod.day) # day
print(tod.weekday()) # weekday

# Hours minutes and seconds
thime = date.time(6,45,30,30) # Time
print(thime)

print(date.datetime.now()) # Current status