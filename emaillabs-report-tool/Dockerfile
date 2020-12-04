FROM python:3.7@sha256:a2ee10f59d79b3d3731c893e1cd1c88187da423a7bbdc61d7ae099f3deadd338
WORKDIR /opt/src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python start.py
