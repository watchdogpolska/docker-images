FROM ruby:2.6.2
RUN gem install travis -v 1.8.9 --no-rdoc --no-ri
RUN travis --version
CMD ["travis","whoami"]
