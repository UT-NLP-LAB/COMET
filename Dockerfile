FROM python:3.10-buster

COPY cache/ /wheels
COPY requirements.txt requirements.txt
COPY checkpoints/  checkpoints/ 
COPY hparams.yaml hparams.yaml

COPY main.py main.py

RUN pip install --no-cache /wheels/*

ENTRYPOINT ["python3.10","main.py"]


