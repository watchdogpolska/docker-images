FROM python:3.7@sha256:cad2e47ce9f5266844285184b799fbae7634d3a469e4effbcadf1ae0aa6ece87
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
