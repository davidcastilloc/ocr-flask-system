# Stage 1: Build stage
FROM python:alpine3.18 as build
LABEL maintainer="David Castillo <vikruzdavid@gmail.com>"
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers tesseract-ocr
COPY requirements.txt ./
RUN pip install -r requirements.txt
# Descargar spa.traineddata y cambiar permisos
RUN wget https://github.com/tesseract-ocr/tessdata_best/raw/main/spa.traineddata -O /usr/share/tessdata/spa.traineddata && \
    chmod +r /usr/share/tessdata/spa.traineddata

# Stage 2: Development stage
FROM build as dev
RUN pip install -r requirements.txt
ENV FLASK_ENV development
ENV FLASK_DEBUG 1
EXPOSE 5000
CMD flask run

# Stage 3: Production stage
FROM build as prod
RUN apk del gcc musl-dev linux-headers
RUN pip install -r requirements.txt
ENV FLASK_ENV production
EXPOSE 5000
CMD gunicorn --certfile=/var/certs/cert1.pem --keyfile=/var/certs/privkey1.pem -w 4 -b 0.0.0.0:5000 app:app
