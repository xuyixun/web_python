# syntax=docker/dockerfile:1

FROM python:slim-buster

WORKDIR /app

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple Flask numpy opencv-python

# Install tesseract library
RUN apt-get install tesseract-ocr -y
# Download last language package
RUN mkdir -p /usr/share/tessdata
ADD https://github.com.cnpmjs.org/tesseract-ocr/tessdata/raw/4.00/chi_sim.traineddata /usr/share/tessdata/chi_sim.traineddata

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]