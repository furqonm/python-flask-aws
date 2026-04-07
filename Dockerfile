FROM public.ecr.aws/docker/library/python:3.12-alpine
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]
