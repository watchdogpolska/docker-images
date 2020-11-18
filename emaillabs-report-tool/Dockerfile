FROM python:3.7@sha256:48eafda05f80010a6677294473d51a530e8f15375b6447195b6fb04dc2a30ce7
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
