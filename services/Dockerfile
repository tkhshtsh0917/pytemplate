FROM python:3.9-alpine

WORKDIR /app

RUN apk update && \
    apk upgrade && \
    apk add --no-cache build-base && \
    pip3 install --no-cache-dir uvicorn fastapi && \
    apk del --purge build-base

COPY mock.py .

EXPOSE 1043

CMD ["uvicorn", "mock:app", "--reload", "--host", "0.0.0.0", "--port", "1043"]
