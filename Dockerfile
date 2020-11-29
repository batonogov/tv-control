FROM batonogov/cron

RUN apt install iputils-ping -y

COPY scheduler/* /usr/local/cron/
