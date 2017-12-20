FROM python:3.6.3-stretch

ADD . /usr/src/

WORKDIR /usr/src

RUN pip install --no-cache-dir -r requirements.txt
