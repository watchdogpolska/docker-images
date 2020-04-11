FROM apache/tika:1.24-full
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get -y install tesseract-ocr-pol \
&& rm -rf /var/lib/apt/lists/*

