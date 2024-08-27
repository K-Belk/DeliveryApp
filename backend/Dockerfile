# Use the official Python 3.11 image as a base
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install uvicorn with the standard option for live reload support
RUN pip install "uvicorn[standard]"

# Copy the FastAPI app code to the container
COPY src/ /app/src

# Expose the FastAPI port
EXPOSE 8000

# Run the FastAPI application with live reload enabled
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
