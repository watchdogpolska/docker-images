FROM python:3.7@sha256:6575824e1a6d55ef9e991153569a3870f04874f4147e7325ec553b80bdd16815
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
