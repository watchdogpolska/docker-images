FROM python:3.8@sha256:f6c7e4926b34f95502fa09aff641931db5f26a98a8f1699a44b79dc4f2aaace9
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]