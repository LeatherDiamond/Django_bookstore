FROM python:3.11.3-slim
ARG group

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt install --no-install-recommends --yes curl gnupg2
RUN useradd -ms /bin/bash newuser && \
    python -m pip install --upgrade pip && \
    pip install poetry

WORKDIR /src
COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false && \
    poetry install --no-root --no-interaction $group

COPY . .

RUN chmod +x entrypoint.sh

USER newuser

ENTRYPOINT [ "./entrypoint.sh" ]

HEALTHCHECK --interval=3s --timeout=10s --start-period=15s --retries=5 \
  CMD curl -f http://localhost:8000/ || exit 1

