# A Simple Example of Django CRUD (Create, Retrieve, Update and Delete) Application Using Functional Based Views



### Demo with swagger
12.0.0.1:8000/swagger/




Steps

1. Run docker using this command - docker-compose up --build
2. Start the Docker containers using docker-compose up, and once the containers are running, open a new terminal and access the Django container
   
   docker exec -it projectgis-web-1 bash
   cd /app  
    python manage.py makemigrations
   python manage.py migrate

3, Test case
python manage.py test your_app_name
