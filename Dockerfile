FROM ubuntu:latest
RUN apt-get update \
    && apt-get install --no-install-recommends --no-install-suggests -y curl \
    && rm -rf /var/lib/apt/lists/*
FROM python:3
ADD Mactest.py /data/
WORKDIR /data
VOLUME /data
ENTRYPOINT [ "python", "/data/Mactest.py"]
