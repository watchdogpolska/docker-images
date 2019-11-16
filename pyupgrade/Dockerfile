FROM python:3.7-slim
RUN pip install pyupgrade
WORKDIR /data
CMD bash -c 'find . -name "*.py" ! \( -wholename "./node_modules/*" -o -wholename "./.tox/*" -o -wholename "./bower_components/*" \) | xargs pyupgrade --py3-only'