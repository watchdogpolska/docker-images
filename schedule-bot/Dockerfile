FROM python:3.8@sha256:29efd1eb1ee5b68683440f3dda64519426539e7839a5d4edb131ddab93cd0f45
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]