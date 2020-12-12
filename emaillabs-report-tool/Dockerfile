FROM python:3.7@sha256:470330af6294963b81e072a33305eaaa906b7b5aa19314332b4f6d998229da9a
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
