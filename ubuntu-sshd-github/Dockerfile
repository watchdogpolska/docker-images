FROM ubuntu:18.10
MAINTAINER Adam Dobrawy "http://github.com/ad-m/"
RUN apt-get update \
&& apt-get install -y openssh-server curl wget git \
&& rm -rf /var/lib/apt/lists/* \
RUN mkdir /run/sshd && mkdir /var/run/sshd && mkdir /root/.ssh
COPY ./entrypoint.sh ./entrypoint.sh
EXPOSE 22
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
