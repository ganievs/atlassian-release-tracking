FROM python:3.10-slim

WORKDIR /src
VOLUME /data

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DATABASE_URL "/data/data.db"

COPY . /src/

RUN pip install pipenv
RUN pipenv install --system

EXPOSE 8000

CMD ["bash", "-c", "alembic upgrade head && uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000"]
