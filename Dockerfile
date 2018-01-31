FROM python:3.6-slim
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/app
RUN rm -rf /var/lib/apt/lists/*
COPY . .
RUN pip install --no-cache-dir -r requirements.txt
