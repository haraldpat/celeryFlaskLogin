FROM python:3.9
COPY requirements.txt /
RUN pip install -r /requirements.txt
ADD . /simple_worker
WORKDIR /simple_worker

ENTRYPOINT celery -A tasks worker --loglevel=info