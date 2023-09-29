FROM python:alpine3.18 as build

LABEL maintainer="David Castillo <vikruzdavid@gmail.com>"

WORKDIR /code

RUN apk add --no-cache gcc  musl-dev linux-headers

RUN apk add tesseract-ocr

RUN wget https://github.com/tesseract-ocr/tessdata_best/raw/main/spa.traineddata -P /usr/share/tessdata/

COPY requirements.txt ./

RUN pip install -r requirements.txt


FROM build as dev
RUN pip install -r requirements.txt
ENV FLASK_ENV development
ENV FLASK_DEBUG 1

FROM base as prod
RUN pip install -r requirements.txt
ENV FLASK_ENV production