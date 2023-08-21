FROM python:3.9-alpine

LABEL maintainer="David Castillo <vikruzdavid@gmail.com>"

WORKDIR /code

ENV FLASK_APP ./app/app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc  musl-dev linux-headers

RUN apk add tesseract-ocr

RUN wget https://github.com/tesseract-ocr/tessdata_best/raw/main/spa.traineddata -P /usr/share/tessdata/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

CMD ["flask", "run"]