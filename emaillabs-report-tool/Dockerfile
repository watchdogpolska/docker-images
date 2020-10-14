FROM python:3.7@sha256:a54a83ddb00879a53b33d2ec4ca8ada540bc9251e80dce276d8caf4ddc326274
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
