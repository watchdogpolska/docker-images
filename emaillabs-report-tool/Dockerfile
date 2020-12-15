FROM python:3.7@sha256:61a6373682a6a375eb232e25121fa42a6d63138ae672212d8ed0c2addfb5f6c6
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
