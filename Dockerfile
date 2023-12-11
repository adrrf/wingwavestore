# Base image
FROM python:3.11

# Set working directory
WORKDIR /app

# Copy the entire project directory
COPY . /app

# Install project dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run the development server
RUN python manage.py migrate
RUN python manage.py loaddata ./fixtures/poblado.json
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]