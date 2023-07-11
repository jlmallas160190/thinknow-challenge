FROM python:3.10-slim-buster

MAINTAINER "Jorge Malla"

RUN apt-get update \
    && apt-get install -yq --no-install-recommends \
    && apt-get install -y --no-install-recommends git=1:2.20.1-2+deb10u3 openssh-client=1:7.9p1-10+deb10u2 \
    && apt-get install gcc=4:8.3.0-1 -y

ENV PYTHONUNBUFFERED 1

RUN useradd -m container_user

RUN mkdir /opt/logs
RUN mkdir /opt/backend
WORKDIR /opt/backend
COPY ./src .
RUN chown -R container_user:container_user /opt/backend
RUN chown -R container_user:container_user /opt/logs

USER container_user

ENV PATH="/home/container_user/.local/bin:${PATH}"


RUN mkdir -p /home/container_user/.ssh/
RUN chmod 700 /home/container_user/.ssh

RUN pip3 install pipenv
RUN pipenv install --system

EXPOSE 8000

ENTRYPOINT ["/opt/backend/entrypoint.sh"]
