FROM python:3.8-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /home
COPY ./requirements.txt .
RUN apk add build-base libffi-dev 
RUN pip install --upgrade pip
RUN --mount=type=cache,target=/root/.cache/pip pip install -r requirements.txt
RUN adduser --disabled-password --no-create-home backend

USER backend
EXPOSE 8000
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 --reload"]