# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Configure pip for better reliability
RUN pip config set global.timeout 120 && \
    pip config set global.retries 3

# Copy project files
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install dependencies using pip with retry logic and timeout
RUN pip install --no-cache-dir --timeout 120 --retries 3 -e . || \
    pip install --no-cache-dir --timeout 120 --retries 3 -e .

# Expose port
EXPOSE 5001

# Set environment variables (these should be overridden at runtime)
ENV ACCESS_TOKEN=""
ENV DEPLOYMENT_ID=""

# Run the server
CMD ["python3", "-m", "xo_mcp_server"] 