# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN python3 -m pytest

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]

EXPOSE 5000

# CMD ["python3", "-m", "gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "--certfile", "/etc/letsencrypt/live/samucaloc.sanp.dev/fullchain.pem", "--keyfile", "/etc/letsencrypt/live/samucaloc.sanp.dev/privkey.pem", "app:app", "--timeout", "120"]