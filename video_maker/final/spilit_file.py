import os
import shutil
from datetime import datetime

import  time
def time_to_string(t):
    return time.strftime("%Y-%m-%d-%H_%M_%S",t)
def string_to_time(t):
    return datetime.strptime(t,"%Y-%m-%d-%H_%M_%S")
for r,d,f in os.walk("../input_img"):
    for file in f:
        if file.endswith('png'):
            t=(string_to_time(file[:-4]))
            if 7 <= t.hour <= 9:
                shutil.copy("../input_img/"+file,'morning')
                shutil.copy("../input_img/"+file,'day')

            elif 17 <= t.hour <= 19:
                shutil.copy("../input_img/"+file,'evening')
                shutil.copy("../input_img/"+file,'day')



