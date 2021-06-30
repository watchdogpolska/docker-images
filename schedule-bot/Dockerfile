FROM python:3.8@sha256:1c67caa564823e87b5729d57d96aa347b8ea3f7caee871da81b4c5b196620f4b
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]