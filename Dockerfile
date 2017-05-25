#FROM armhf/alpine:3.5
FROM alpine:3.3
MAINTAINER cma <cma@maxleap.com>
# Update
RUN apk add --update python py-pip \
    && pip install --upgrade pip \
    && rm /var/cache/apk/*

# Install app dependencies
RUN mkdir -p /opt/itchatRobot
WORKDIR /opt/itchatRobot
RUN mkdir logs
ADD wheels/ wheels
ADD requirements.txt .
RUN pip install wheel
RUN pip install --use-wheel --no-index --find-links=wheels -r requirements.txt

ADD robots robots
ADD run.py .
ENTRYPOINT ["python", "run.py"]