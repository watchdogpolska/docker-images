FROM python:3.9@sha256:0813df59b3d73a13fc581fd416d7733a2de6540d7e3f7633a1a9aabf9b201548
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
