# base image  
FROM python:3.10   
# setup environment variable  
ENV DockerHOME=/home/app/webapp  

# set work directory  
RUN mkdir -p $DockerHOME  

# where your code lives  
WORKDIR $DockerHOME

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . $DockerHOME
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  
EXPOSE 8000

#ENTRYPOINT ["python","/home/app/webapp/manage.py"]
#makeMigrationDB
CMD python3 manage.py makemigrations restaurant;python3 manage.py migrate;python3 manage.py runscript add_restaurants; python3 manage.py runserver 0.0.0.0:8000;


#migrate db#CMD ["python3", "manage.py migrate"]

#add entries
#CMD ["python3"," manage.py runscript add_restaurants"]


# start server  
#CMD python3 manage.py runserver

#CMD python3 manage.py makemigrations restaurants
 
