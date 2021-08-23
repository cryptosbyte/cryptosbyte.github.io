# Cryptos' Blog

This is my blog website (which I sadly cannot run currently but maybe in the future) which will contain articles, lifestyle, etc. Feel free to contribute to this project/app by sending a commit.
If you'd like to run the server: 
###### first install the packages...
```sh
$ python3 -m pip install -r requirements
```
###### And then initalise the database...
```sh
$ chmod 755 ./db_setup.sh
$ ./db_setup.sh
```
###### And run the Flask App
```sh
$ gunicorn app:app
$ # Or alternatively
$ python3 app.py
```