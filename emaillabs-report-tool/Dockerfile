FROM python:3.7@sha256:213cba0233e4f6f0a274425c245d74f6140a6fa798df487708327a489a58deb7
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
