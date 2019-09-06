FROM python:3.7-slim-buster
COPY . /app
WORKDIR /app
RUN ./create_index.sh
CMD python3 -m http.server 8080
