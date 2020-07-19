FROM python:3.7
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
