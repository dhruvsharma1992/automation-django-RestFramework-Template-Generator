automation-django-RestFramework-Template-Generator
==================================================
#####Requirements

Pip to be installed and added to environment variables 

Python 2.7
#####Steps to use
1) If you don't have django and/or RestFramework  installed,  run setup.bat.

2) Then run  test.bat and you're done :) .  To run  test.bat type:

```test.bat <app-name>```

3 ) To test the installations and  run the  project/server 

``` cd <folder with appname>```

```python manage.py runserver 0.0.0.0:<port> ``` 

You  can use  port between 1000 to 56K.  Ideally  we  use  port 8000 or 8080 

#####Features
1) you can check the output using 
```localhost:<port>\test``` which shows a sample get query which renders an index html page with a list and a dict rendered on the page. The code for the same can be found in views.py ( class test) and templates\index.html

2) ```localhost:<port>\get?parameter=12345``` is an example of a get query with query parameters. The  api  returns an application/json with same data as passed in the 'parameter' argument.

3) ```localhost:<port>\post``` is an  example of a Post request.  You  have  to  use either a rest console\postman\ any other extension to fire a  post request or you can use an ajax query from your  browser's console.  It  returns  the  data  passed as payload  as an  application/json.


#####To contribute
1) Fork the repo.

2) Create a branch

 3)  Send a pull request after making your changes.

**(Check the  issues  to understand the  current   pending    works )
