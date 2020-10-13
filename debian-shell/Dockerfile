FROM debian:10.5@sha256:2f53b5f0101a2f296c632c28010df43575b8ced96615b4b0b370d52a7004f473
RUN apt-get update \
&& apt-get install -y --no-install-recommends ca-certificates rsync curl wget nano locales \
&& rm -rf /var/lib/apt/lists/*
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
&& dpkg-reconfigure --frontend=noninteractive locales \
&& update-locale LANG=en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
