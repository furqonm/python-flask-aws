FROM public.ecr.aws/bitnami/python:2.7.18
WORKDIR /project
ADD . /project
RUN pip install -r requirements.txt
ENTRYPOINT ["python","app.py"]