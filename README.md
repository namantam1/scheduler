# scheduler
A Django application API which schedule a url for sending a get request at a particular time.

## Installing setup

```bash
pip install -r requirements.txt
```
##### Now run the following commands to run server
```bash
python manage.py runserver
 ```
 ##### Now after starting the server you have to start process_tasks to make the get request on the scheduled time
 ```bash
 python manage.py process_tasks
 ```
 
 #### Now open postman and send the following request - 
 
 1. First to check whether server is alive send a ping request to http://127.0.0.1:8000/ping if it returns a status ok response the server is alive.
 2. Now to send a url as parameter set parameter key as **url** and parameter as the url which you want to send and for setting the time use key **datetime** 
    and for setting the date in the format **yyyy/mm/ddThh:min**.
 ##### For example - 
 >key  =   datetime \
 >parameter = 2020/06/23T17:50        ( To set the time 5:50 pm and date 23rd june, 2020 ) 
 
  Now if it returns the same parameter back as json then your request has been successful otherwise it will show the corresponding error.
  
  ## The Package used in the project
  1. django
  2. djangorestapi
  3. background-tasks
