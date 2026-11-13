# FROM python:3.10-slim

# WORKDIR /app

# # Install your dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy your Python code, HTML, and ONNX model
# COPY . .

# # Google Cloud Run assigns a dynamic port via the $PORT variable
# CMD uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}


FROM python:3.10-slim

WORKDIR /app

# Install dependencies first (helps Docker caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application and model files
COPY . .

# Start the FastAPI application
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-8080}"]
