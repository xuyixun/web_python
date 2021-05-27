# syntax=docker/dockerfile:1

FROM python:slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN pip install Flask
RUN pip install opencv-python

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]