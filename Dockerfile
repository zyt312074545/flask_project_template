# Base image
FROM python:3.7.1-alpine3.8
MAINTAINER zyt

# Install compile environment
RUN apk add --no-cache gcc musl-dev libffi-dev openssl-dev jpeg-dev zlib-dev
## docker's timezone use UTC, but our timezone is CST, so we need to reset docker's zonetime.
RUN apk add --no-cache tzdata
RUN cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime && echo 'Asia/Shanghai' >/etc/timezone

# Copy Pipfile and install packages use Pipfile
ARG PROJECT=project
RUN mkdir -p /${PROJECT}
COPY Pipfile /${PROJECT}
RUN pip3 install --upgrade pip \
    && pip3 install pipenv \
    && pipenv install --skip-lock \
    && pipenv install gunicorn --skip-lock

# Copy project and Set project environment
COPY . /${PROJECT}
WORKDIR /${PROJECT}
EXPOSE 5000

# Set development volume
VOLUME ["/${PROJECT}"]

# Run project
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:5001", "api:app", "--preload"]
