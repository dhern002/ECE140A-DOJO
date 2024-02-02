FROM python:3.8

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt
RUN pip install watchdog

COPY . /app

CMD ["watchmedo", "auto-restart", "--directory=./", "--pattern=*.py;*.txt", "--recursive", "--", "python", "main.py"]

