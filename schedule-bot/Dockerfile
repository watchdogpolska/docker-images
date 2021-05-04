FROM python:3.8@sha256:3af414fe92928a6ea49876d3e4268d9647901ada92eced00dd3aef47d53390c0
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]