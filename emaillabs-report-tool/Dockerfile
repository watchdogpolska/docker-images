FROM python:3.7@sha256:f9357b036aaab5142a34942f6f64033d50823f52ab8414d6a6c4371ea0c7f862
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
