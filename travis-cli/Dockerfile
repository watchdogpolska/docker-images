FROM ruby:2.7.1@sha256:915dfd096c156c2b151ee236b5daa1085d17ded7646e77622ccd351da951335d
RUN gem install travis -v 1.8.9
RUN travis --version
CMD ["travis","whoami"]
