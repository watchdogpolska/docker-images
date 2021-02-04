FROM ruby:2.7.1@sha256:b3aab6a052e2397456342d97a4d0591d4b2bf54b1ee6e599867fb95440f22a6c
RUN gem install travis -v 1.8.9
RUN travis --version
CMD ["travis","whoami"]
