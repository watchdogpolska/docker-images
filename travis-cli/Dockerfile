FROM ruby:2.7.3@sha256:ee2b19ced1d44600963c52691b9b6975e209286e7168230d03afe7894f9c81a0
RUN gem install travis -v 1.8.9
RUN travis --version
CMD ["travis","whoami"]
