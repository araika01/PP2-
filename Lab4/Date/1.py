import datetime
today = datetime.datetime.now()
day1 = today - datetime.timedelta(1)
day2 = today - datetime.timedelta(2)
day3 = today - datetime.timedelta(3)
day4 = today - datetime.timedelta(4)
day5 = today - datetime.timedelta(5)
print("five days from current date: ", today)
print(day1)
print(day2)
print(day3)
print(day4)
print(day5)