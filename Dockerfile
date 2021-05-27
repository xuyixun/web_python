# syntax=docker/dockerfile:1

FROM python:slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install Flask numpy opencv-python

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]