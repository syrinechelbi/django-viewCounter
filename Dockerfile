FROM python:3.9

# Set the working directory to the folder where manage.py is located
WORKDIR /app/cool_counters

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install -r /app/requirements.txt

# Copy the rest of the project (ensure manage.py and other files are copied)
COPY . /app/

# Ensure the static files directory exists
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --no-input

# Apply migrations
RUN python manage.py migrate

# Expose the port for the application
EXPOSE 8000

# Command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
