FROM debian:10.7@sha256:b16f66714660c4b3ea14d273ad8c35079b81b35d65d1e206072d226c7ff78299
RUN apt-get update \
&& apt-get install -y --no-install-recommends ca-certificates rsync curl wget nano locales \
&& rm -rf /var/lib/apt/lists/*
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
&& dpkg-reconfigure --frontend=noninteractive locales \
&& update-locale LANG=en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
