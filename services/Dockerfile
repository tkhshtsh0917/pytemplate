FROM python:3.9-alpine

WORKDIR /app

ADD . /app

RUN apk update && \
    apk upgrade && \
    apk add --no-cache build-base && \
    pip3 install --no-cache-dir uvicorn fastapi && \
    apk del --purge build-base

EXPOSE 8000

CMD ["uvicorn", "mock:api", "--reload", "--host", "localhost", "--port", "8000"]
