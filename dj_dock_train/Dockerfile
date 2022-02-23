FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#ARG APP_PORT = 8000
#ENV APP_PORT = $APP_PORT
#RUN python3 manage.py runserver 0.0.0.0:$APP_PORT
#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]