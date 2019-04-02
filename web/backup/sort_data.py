import datetime
import re
import threading

from web.backup.config import *

keys = redis.keys('gaode:*')
times_arr = []
time_format = "%Y-%m-%d-%H_%M_%S"
for k in keys:
    pattern = re.compile('gaode:(.+)')
    time = re.search(pattern, k).group(1)
    time = datetime.datetime.strptime(time, time_format)
    times_arr.append(time)
times_arr = sorted(times_arr)
begin_date = times_arr[0]
end_date = times_arr[-1]


def gen_hname(time):
    return 'gaode:%s' % time.strftime(time_format)


def get_moring(day=4):
    data = []
    with open('%s_moring.txt' % day, 'w')as f:
        for t in times_arr:
            if t.hour in [7, 8, 9] and t.day == day:
                t = gen_hname(t)
                print(t)
                data.append(eval(redis.hget(t, 'points')))
        f.write(str(data))


def get_evening(day=4):
    data = []
    with open('%s_evening.txt' % day, 'w')as f:
        for t in times_arr:
            if t.hour in [17, 18, 19] and t.day == day:
                t = gen_hname(t)
                print(t)
                data.append(eval(redis.hget(t, 'points')))
        f.write(str(data))


def get_allday(day=4):
    data = []
    flag=0
    with open('%s_day.txt' % day, 'w')as f:
        for t in times_arr:
            if t.day == day:
                flag = 1
                t = gen_hname(t)
                print(t)
                data.append(eval(redis.hget(t, 'points')))
            else:
                if flag==1:
                    break
        f.write(str(data))


def startthread(graph_list):
    print(len(graph_list))
    threadlist = []
    for g in graph_list:
        t = threading.Thread(target=get_allday, args=(g,))
        t.setDaemon(True)
        threadlist.append(t)
    for t in threadlist:
        t.start()
    for j in threadlist:
        j.join()



graph_list=[]

startthread([i for i in range(4,12)])


