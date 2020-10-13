FROM python:3.8@sha256:31f1886d4d20eb2a8639ed3597ea973315c2edb272014f5c80aa7afdfdc6c676
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]