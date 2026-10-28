FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir "anthropic>=2.1.0"
COPY archibald ./archibald
COPY demo ./demo
ENV HOST=0.0.0.0 PORT=8000 ARCHIBALD_DB=/data/archibald.db PYTHONUNBUFFERED=1
RUN mkdir -p /data
EXPOSE 8000
CMD ["python", "-m", "archibald.cli", "serve"]
