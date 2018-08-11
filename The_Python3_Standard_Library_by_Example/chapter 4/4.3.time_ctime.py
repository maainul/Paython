import time

print(time.ctime())
later = time.time()+15
print('15 secs from now:', time.ctime(later))
