FROM ubuntu:16.04
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y python3-pip \
	&& pip3 install pika \
	&& apt-get update \
	&& apt-get install -y rabbitmq-server

ADD producer.py /
CMD [ "tail -F /dev/null" ]