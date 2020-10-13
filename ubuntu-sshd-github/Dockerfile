FROM ubuntu:18.04@sha256:45c6f8f1b2fe15adaa72305616d69a6cd641169bc8b16886756919e7c01fa48b
MAINTAINER Adam Dobrawy "http://github.com/ad-m/"
RUN apt-get update \
&& apt-get install -y openssh-server curl wget git less \
&& rm -rf /var/lib/apt/lists/* \
RUN mkdir /run/sshd && mkdir /var/run/sshd && mkdir /root/.ssh
COPY ./entrypoint.sh ./entrypoint.sh
EXPOSE 22
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
