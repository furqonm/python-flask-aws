FROM public.ecr.aws/docker/library/python:3.10.1-alpine
WORKDIR /project
ADD . /project
RUN apk add --update curl && \
    pip install -r requirements.txt
CMD ["python","app.py"]