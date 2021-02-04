FROM python:3.5@sha256:42a37d6b8c00b186bdfb2b620fa8023eb775b3eb3a768fd3c2e421964eee9665 as builder
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv lock --requirements > /requirements.txt
FROM python:3.5@sha256:42a37d6b8c00b186bdfb2b620fa8023eb775b3eb3a768fd3c2e421964eee9665 as app
WORKDIR /opt/src
COPY --from=builder /requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD python export_table.py