# syntax=docker/dockerfile:1

FROM python:slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -i https://pypi.doubanio.com/simple/ --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]