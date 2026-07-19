FROM python:3.11-alpine

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir flask gunicorn

# Copy application files
COPY app.py .
COPY templates/ templates/

# Expose the default application port
EXPOSE 8097

# Set up persistence volume
VOLUME /app/data

# Run the production server
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8097", "app:app"]
