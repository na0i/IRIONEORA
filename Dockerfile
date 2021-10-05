# FROM sjoh004/django:latest
FROM python:3.8
RUN apt-get -y update && apt-get -y install default-jdk
RUN pip3 install django
WORKDIR /usr/src/app

COPY . .
RUN pip install -r ./backend/requirements.txt

WORKDIR ./backend
CMD ["spark-submit", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000