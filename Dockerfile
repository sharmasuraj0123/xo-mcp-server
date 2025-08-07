# Use Python 3.11 slim image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml README.md ./
COPY src/ ./src/

# Install dependencies using pip
RUN pip install --no-cache-dir -e .

# Expose port
EXPOSE 5000

# Set environment variables (these should be overridden at runtime)
ENV ACCESS_TOKEN=""
ENV DEPLOYMENT_ID=""

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:5000/health || exit 1

# Run the server
CMD ["python3", "-m", "xo_mcp_server"] 