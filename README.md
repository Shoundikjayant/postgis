# A Simple Example of Django CRUD (Create, Retrieve, Update and Delete) Application Using Functional Based Views

We will use Django and functional based views to develop a simple application to allow one to create a new task, retrieve task list or a single task, update a task and delete a task.

### Demo

If you cannot see the animated gif below, please download task_crud.gif and open it in our browser.
Steps

1. Run docker using this command - docker-compose up --build
2. Start the Docker containers using docker-compose up, and once the containers are running, open a new terminal and access the Django container
   docker exec -it projectgis-web-1 bash
   cd /app  
    python manage.py makemigrations
   python manage.py migrate

3, Test case
python manage.py test your_app_name
