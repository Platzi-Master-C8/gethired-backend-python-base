FROM python:3.7
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app
RUN mkdir /app/requirements/
COPY ./requirements /app/requirements/

RUN pip install -r requirements/production.txt
COPY . /app/

CMD python main.py
