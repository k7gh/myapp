# Use a lightweight Python image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Copy code and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

# Expose port and run
EXPOSE 5000
CMD ["python", "app.py"]
