FROM python:3.8@sha256:82ced8a8928fd8197228f9d488b7c4efefc4ed3b51f2288a42bfaabbec242fdf
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./lib .
CMD ["python", "main.py"]