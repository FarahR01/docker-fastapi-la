FROM python:3.12-slim

LABEL maintainer="you@example.com"
LABEL version="1.0"

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies (cached layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and ensure proper permissions
# prefer addgroup/adduser on Debian-based slim images
RUN addgroup --system app && adduser --system --ingroup app app \
		&& mkdir -p /app

# Copy application code and set ownership to the non-root user
COPY --chown=app:app app ./app

USER app

EXPOSE 8000

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
	CMD curl -f http://127.0.0.1:8000/health || exit 1

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
