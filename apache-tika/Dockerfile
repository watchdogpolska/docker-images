FROM apache/tika:1.25-full@sha256:7a7f4a017e59af1d36c1368ed681d335f22ca909004d9cc9a6a2b21eb0fb808a
RUN apt-get update \
&& DEBIAN_FRONTEND=noninteractive apt-get -y install tesseract-ocr-pol \
&& rm -rf /var/lib/apt/lists/*

