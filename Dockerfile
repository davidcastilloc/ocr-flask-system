FROM python:alpine3.18 as build

LABEL maintainer="David Castillo <vikruzdavid@gmail.com>"

WORKDIR /src

RUN apk add --no-cache gcc  musl-dev linux-headers

RUN apk add tesseract-ocr

RUN wget https://github.com/tesseract-ocr/tessdata_best/raw/main/spa.traineddata -P /usr/share/tessdata/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt