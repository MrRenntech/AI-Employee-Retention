# Use official Python 3.10 image as a base
FROM python:3.10-slim

# Set environment variables for production
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/app

# Create and set the work directory
WORKDIR /app

# Install system dependencies (e.g. for native ML compiling if needed)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

# Copy the requirements file and install explicit dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose standard production port
EXPOSE 5000

# Initialize the database (Creates the SQLite DB and an admin user)
RUN python app/init_db.py

# Run the High-Performance WSGI server
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "3", "app.app:app"]
