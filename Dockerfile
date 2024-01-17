# Use an official Python runtime as a parent image

FROM python:3.8

# Install GDAL dependencies
RUN apt-get update && apt-get install -y libgdal-dev && apt-get clean && rm -rf /var/lib/apt/lists/*

# Set environment variables required by GDAL
ENV CPLUS_INCLUDE_PATH=/usr/include/gdal
ENV C_INCLUDE_PATH=/usr/include/gdal

# Install GDAL using pip
RUN pip install GDAL==3.2.2 --no-binary :all:

RUN pip install --upgrade pip





# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app/
# Install any needed packages specified in requirements.txt
RUN pip install --upgrade setuptools pip
RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py makemigrations tasks

# Expose port 8000 to the outside world
EXPOSE 8000
EXPOSE 3306

# Run app.py when the container launches
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
