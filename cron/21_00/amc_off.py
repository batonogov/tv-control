import sys, os
sys.path.insert(0, "/usr/local/cron/tv_control")
from AMC import *


amc_list = '/usr/local/cron/tv_list/amc_list'
port = 2525

tv_list = []

with open(amc_list) as amc:
    for line in amc:
        tv_list.append(line)

for tv in tv_list:
    response = os.system('ping -c 1 ' + tv)
    if response == 0:
        send_command(power_off, tv, port)
    else:
        print('Устройство', tv, 'недоступно.')
