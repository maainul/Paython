import datetime
today=datetime.date.today()
print(today)
one_day = datetime.timedelta(days=1)
yestarday = today-one_day
print(yestarday)
tomorrow = today+one_day
print(tomorrow)
