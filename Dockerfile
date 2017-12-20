FROM python:3.6.3-stretch

WORKDIR ./

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ADD . ./

CMD [ "python", "./manage.py", "runserver", "0.0.0.0:80"]