# FROM sjoh004/django:latest
FROM python:3.8
RUN pip3 install django
WORKDIR /usr/src/app

COPY . .
RUN pip install -r requirementss.txt

WORKDIR ./backend
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000