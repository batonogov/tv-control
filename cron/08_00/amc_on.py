import sys
sys.path.insert(0, "/usr/local/cron/tv_control")
from AMC import *


amc_list = '/usr/local/cron/tv_list/amc_list'
port = 2525

with open(amc_list) as amc:
    for line in amc:
        print(line)
        print(send_command(power_on, line, port))
