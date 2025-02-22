FROM alpine:latest
RUN apk --update add apache2
RUN rm -rf /var/cache/apk/*
ENTRYPOINT [ "httpd", "-D", "FOREGROUND" ]