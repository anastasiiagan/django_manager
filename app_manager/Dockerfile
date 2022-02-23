FROM python:3.8-slim-buster

WORKDIR /app_manager

COPY . /app_manager

RUN pip3 install -r requirements.txt

RUN pip install docker

CMD ["python3", "app_manager.py"]