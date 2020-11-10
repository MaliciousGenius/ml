FROM alpine
RUN apk update ; \
    apk upgrade ; \
    apk add --no-cache ca-certificates ; \
    update-ca-certificates 2>/dev/null || true ; \
    apk add --no-cache python2 python3 ; \
    apk add cmd:pip2 ; \
    apk add cmd:pip3 ; \
    pip3 install clickhouse_driver ;
RUN touch /var/log/cron.log
ADD crontab /etc/crontab
RUN /usr/bin/crontab /etc/crontab
CMD /usr/sbin/crond -f -L /var/log/cron.log
