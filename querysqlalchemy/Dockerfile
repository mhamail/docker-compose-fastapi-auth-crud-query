FROM python:3.12

WORKDIR /code

# Install system dependencies required for potential Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

ENV PIP_DEFAULT_TIMEOUT=120

RUN pip install poetry

COPY . /code/

RUN poetry install

# EXPOSE  8000:9000

CMD ["poetry", "run", "uvicorn", "querysqlalchemy.main:app", "--host", "0.0.0.0", "--reload"]
