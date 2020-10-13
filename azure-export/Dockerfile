FROM python:3.5@sha256:24d62b9e24e5b601b524f33a1d477a66fce675efe11c96dd163c0f0ce5cc9810 as builder
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > /requirements.txt
FROM python:3.5@sha256:24d62b9e24e5b601b524f33a1d477a66fce675efe11c96dd163c0f0ce5cc9810 as app
WORKDIR /opt/src
COPY --from=builder /requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python export_table.py