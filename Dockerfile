FROM public.ecr.aws/docker/library/python:3.11.0b1-alpine3.15
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]