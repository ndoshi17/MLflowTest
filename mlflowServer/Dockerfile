FROM ubuntu:18.04


RUN apt-get update && apt-get upgrade -y
RUN apt-get install python 3.7.0 -y
RUN apt-get install python3-pip -y
RUN apt-get install libpq-dev python-dev -y
COPY requirements.txt /
RUN pip3 install -r requirements.txt
COPY ./startup.sh /
RUN chmod +x /startup.sh

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

ENV PORT 5000
ENV AWS_BUCKET bucket

ENTRYPOINT ["/startup.sh"]
