import datetime
import time

dt = datetime.datetime.now()
print(dt)

print(dt.day, dt.month, dt.year, dt.hour, dt.minute, dt.second)

ds = datetime.datetime.fromtimestamp(time.time())
print(ds)

td = datetime.timedelta(days=11, hours=5, minutes=12, seconds=8)
print(td)

ma = st.strftime('%Y/%m/%d %H:%M:%S %p')
print(ma)
