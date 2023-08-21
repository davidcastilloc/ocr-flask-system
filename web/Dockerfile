FROM python:3.9-alpine

LABEL maintainer="David Castillo <vikruzdavid@gmail.com>"

WORKDIR /code

ENV FLASK_APP ./app/app.py

ENV FLASK_RUN_HOST 0.0.0.0

RUN apk add --no-cache gcc  musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt 

CMD [ "flask" "run" ]