This web-based project was done for the purpose of a college project, the purpose of the study is to learn how to do full stack development using tools and frameworks to do the job. For this project, the tool that was used was phpMyAdmin. phpMyAdmin was used to both create and manage the database that will be interacting with the web.
The framework that was used to run the web is the Flask library in Python. As the web was built and designed to be very simple, the best framework to be used seem to be flask in contrast to popular ones like laravel as laravel is seemingly overkill for this level of complexity.
To run the app, make sure that python is installed as well as Flask. Commands to install libraries:

- pymysql library - pip install PyMySQL
- Flask - pip install flask
- Flaskext - pip install Flask-MySQL
- bcrpt - pip install flask-bcrypt

You are welcome to use the users in the dummy database, although since they are all encrypted, make sure to take note of the passwords. The passwords in the default dummy database are all '12345' without the quotation marks.
As for the mySQL file, it is in the directory named as 'dummyDatabase' for use, before running the app make sure to import the mySQL file into any database tools and to change the configuration in 'app.py' according to the name or tool that was used.