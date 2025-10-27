# Lightweight Dockerfile for the FastAPI application
# - Uses python:3.11-slim
# - Installs runtime dependencies, copies app code, and runs uvicorn

FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
	PYTHONUNBUFFERED=1

RUN apt-get update \
	&& apt-get install -y --no-install-recommends curl gcc libc-dev \
	&& rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip \
	&& pip install --no-cache-dir -r requirements.txt

# Copy application source
COPY . /app

# Create a non-root user and switch to it
RUN addgroup --system app && adduser --system --group app || true \
	&& chown -R app:app /app
USER app

EXPOSE 80

# Simple HTTP healthcheck that queries the health endpoint
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:80/healthz || exit 1

# Run the app with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]


