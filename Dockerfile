FROM public.ecr.aws/docker/library/python:alpine3.15
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]