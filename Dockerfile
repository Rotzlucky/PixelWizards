FROM jekyll/jekyll:4.2.0

WORKDIR /srv/jekyll

COPY Gemfile* ./
RUN bundle install

EXPOSE 4000

CMD ["jekyll", "serve", "--livereload", "--host", "0.0.0.0"]