FROM alpine as builder

RUN apk update && apk add wget gcc make libc-dev

WORKDIR /app
RUN wget -O - http://www.no-ip.com/client/linux/noip-duc-linux.tar.gz | tar -xzf -
RUN cd noip-*/ \
	&& make \
	&& mkdir /usr/local/etc \
	&& cp noip2 /usr/local/bin/noip2


FROM alpine

RUN mkdir /usr/local/etc
COPY --from=builder /usr/local/bin/noip2 /usr/local/bin/noip2
RUN apk add --update libintl && apk add --virtual build_deps gettext

ENTRYPOINT /usr/local/bin/noip2 -C -u $USERNAME -p $PASSWORD -U $INTERVAL -Y \
	&& /usr/local/bin/noip2 \
	&& while kill -0 $(pgrep noip2) 2> /dev/null; do sleep 5; done
