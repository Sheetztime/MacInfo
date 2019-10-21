FROM python:3
ADD Mactest.py /data/
WORKDIR /data
VOLUME /data
ENTRYPOINT [ "python", "/data/Mactest.py"]
