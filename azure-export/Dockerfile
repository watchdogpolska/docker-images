FROM python:3.8 as builder
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > /requirements.txt
FROM python:3.8 as app
WORKDIR /opt/src
COPY --from=builder /requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python export_table.py