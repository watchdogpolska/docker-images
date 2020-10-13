FROM python:3.7@sha256:0ae19ba45dafa947c830aa3e7956770786d650d90a01e2309c0fb2bc70e30cf3
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
