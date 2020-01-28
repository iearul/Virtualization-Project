# Project Virtualization

To Run the project we need docker-compose

#First We run the below command to build our project

docker-compose up -d --build

#We can check our container with this command

docker ps -a

#We have to exceute our app with this command

docker exec -it virt_project_app_1 /bin/bash

#In another terminal we execute same container to publish data with below 2 command

docker exec -it virt_project_app_1 /bin/bash

python3 glue-app/main.py

#In 1st terminal we run this command to subcribe some data(we can use any range)

python3 app/main.py 10 60


#We use another terminal to check database 

docker exec -it virt_project_mongodb_1 /bin/bash

mongo

show dbs

use primedb

show collections

db.primecollection.find()
