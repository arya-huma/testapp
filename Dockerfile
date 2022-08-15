FROM python:3.8-bullseye

COPY ./requirements.txt /app/requirements.txt
COPY ./templates/ /app/templates/
COPY ./static /app/static/

WORKDIR /app

RUN pip install -r requirements.txt

COPY ./app.py /app/


WORKDIR /app
CMD [ "python", "app.py" ]