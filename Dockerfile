FROM python:3.10-slim

WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY Pipfile Pipfile.lock /src/
COPY src/ /src/

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000

ENTRYPOINT ["uvicorn", "app.main:app"]

CMD ["--reload", "--workers 1", "--host 0.0.0.0", "--port 8000"]
