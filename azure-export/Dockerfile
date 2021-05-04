FROM python:3.9@sha256:0813df59b3d73a13fc581fd416d7733a2de6540d7e3f7633a1a9aabf9b201548 as builder
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > /requirements.txt
FROM python:3.9@sha256:0813df59b3d73a13fc581fd416d7733a2de6540d7e3f7633a1a9aabf9b201548 as app
WORKDIR /opt/src
COPY --from=builder /requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python export_table.py