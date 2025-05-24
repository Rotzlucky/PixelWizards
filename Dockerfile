FROM jekyll/jekyll:4.2.0

USER root
RUN chown -R jekyll:jekyll /srv/jekyll

USER jekyll
WORKDIR /srv/jekyll

COPY --chown=jekyll:jekyll Gemfile* ./
RUN bundle install

EXPOSE 4000

CMD ["bundle", "exec", "jekyll", "serve", "--livereload", "--host", "0.0.0.0"]