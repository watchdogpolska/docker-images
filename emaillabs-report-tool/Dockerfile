FROM python:3.7@sha256:5caf7aceb1d01f45686491e24528edf13878508390fcf37a39ac98d69a842bb4
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
