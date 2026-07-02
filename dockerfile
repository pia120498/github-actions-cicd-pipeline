# ---------- Stage 1 : Install Dependencies ----------
FROM python:3.13-slim AS builder

WORKDIR /app

COPY app/requirements.txt .

RUN pip install --no-cache-dir \
    --prefix=/install \
    -r requirements.txt


# ---------- Stage 2 : Runtime ----------
FROM python:3.13-slim

WORKDIR /app

COPY --from=builder /install /usr/local

COPY app/ .

EXPOSE 5000

HEALTHCHECK --interval=30s --timeout=5s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:5000/health')"

CMD ["python", "app.py"]