FROM apache/tika:1.24-full@sha256:ec1d21a188501ccfc78299973b314ea8ac4111c224b958c0ef9d6e8d31b8d8d8
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get -y install tesseract-ocr-pol \
&& rm -rf /var/lib/apt/lists/*

