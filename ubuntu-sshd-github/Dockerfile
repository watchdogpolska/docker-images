FROM ubuntu:18.04@sha256:a7fa45fb43d471f4e66c5b53b1b9b0e02f7f1d37a889a41bbe1601fac70cb54e
MAINTAINER Adam Dobrawy "http://github.com/ad-m/"
RUN apt-get update \
&& apt-get install -y openssh-server curl wget git less \
&& rm -rf /var/lib/apt/lists/* \
RUN mkdir /run/sshd && mkdir /var/run/sshd && mkdir /root/.ssh
COPY ./entrypoint.sh ./entrypoint.sh
EXPOSE 22
ENTRYPOINT ["./entrypoint.sh"]
CMD ["/usr/sbin/sshd", "-D"]
