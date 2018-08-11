import time

def show_struct(s):
    print('   year:',s.tm_year)
    print('   Month:',s.tm_mon)
    print('   Date:',s.tm_mday)
    print('   Hour:',s.tm_hour)
    print('   min:',s.tm_min)
    print('   Second:',s.tm_sec)
    print('   week:',s.tm_wday)
    print('   year day:',s.tm_yday)


#print('gmtime')
show_struct(time.gmtime())
#show_struct(time.localtime())
