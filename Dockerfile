FROM python:3.7-slim-buster

ADD . /app

RUN python3 -m pip install -r /app/requirements.txt

WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "rithm.wsgi"]