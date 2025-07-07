# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy backend and frontend templates/static
COPY ./backend /app/backend
COPY ./frontend/templates /app/frontend/templates
COPY ./frontend/static /app/frontend/static

# Install dependencies
RUN pip install --no-cache-dir -r /app/backend/requirements.txt

# Set environment variables
ENV FLASK_APP=/app/backend/app.py
ENV FLASK_RUN_PORT=5000

# Expose the Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "/app/backend/app.py"]
