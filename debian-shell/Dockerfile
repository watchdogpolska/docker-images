FROM debian:10.6@sha256:60cb30babcd1740309903c37d3d408407d190cf73015aeddec9086ef3f393a5d
RUN apt-get update \
&& apt-get install -y --no-install-recommends ca-certificates rsync curl wget nano locales \
&& rm -rf /var/lib/apt/lists/*
RUN sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
&& dpkg-reconfigure --frontend=noninteractive locales \
&& update-locale LANG=en_US.UTF-8
ENV LANGUAGE en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8
