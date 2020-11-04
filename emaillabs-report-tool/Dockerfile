FROM python:3.7@sha256:f571443e5baf71b7e9602f00ec4d743634cace0d50e5688c33a1caf365b4a77c
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
