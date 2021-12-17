FROM public.ecr.aws/docker/library/python:3.10.1-alpine
WORKDIR /project
ADD . /project
RUN apk --no-cache add curl && \
    pip install -r requirements.txt
CMD ["python","app.py"]