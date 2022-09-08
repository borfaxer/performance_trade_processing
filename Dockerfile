
FROM ubuntu:22.04

RUN apt update

RUN apt-get -y install software-properties-common python3.10 python3-pip vim pypy3

