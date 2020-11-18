FROM python:3.8@sha256:104453cedda589cfb77b2becc521f2975fbd933e7caa7912633b4c64aab103e5
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]