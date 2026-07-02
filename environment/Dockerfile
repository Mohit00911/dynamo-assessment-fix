# Pinned to a specific SHA256 digest for reproducibility.
FROM python@sha256:9c7a52d9198642a8b9fbd2f01fbd8fba816d9b23b12853245f784e2a878505e8

RUN pip install --no-cache-dir pytest==8.4.1 pytest-json-ctrf==0.3.5

WORKDIR /app

COPY access.log /app/access.log