FROM ruby:2.7.3@sha256:e57b8922ec57a9116cdd8295c041a6cbf84ce7a8baf5e521e845e3bd0bae9127
RUN gem install travis -v 1.8.9
RUN travis --version
CMD ["travis","whoami"]
