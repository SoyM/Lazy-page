FROM debian:stretch
FROM python:3.6.3-stretch
FROM httpd:latest
FROM mysql:5

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . .

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]