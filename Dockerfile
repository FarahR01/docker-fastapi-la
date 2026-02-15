FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Create a non-root user and ensure proper permissions
RUN groupadd -r app && useradd -r -g app app \
	&& mkdir -p /app

# Copy application code and set ownership to the non-root user
COPY --chown=app:app app ./app

USER app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
