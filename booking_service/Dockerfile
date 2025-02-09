FROM python:3.11-slim

WORKDIR /app

RUN pip install poetry

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root


COPY . /app

EXPOSE 8000

ENV PYTHONUNBUFFERED=1

CMD ["python", "./main.py"]