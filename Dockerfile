FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED 1

# Download latest listing of available packages:
RUN apt-get -y update
# Upgrade already installed packages:
RUN apt-get -y upgrade
# Install a new package:
RUN apt-get -y install vim net-tools

RUN pip install pip -U

RUN mkdir /root/.kube/

COPY code /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN rm requirements.txt
