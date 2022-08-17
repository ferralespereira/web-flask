# Flask
This is a web site made it in Flask with the goal of make a CRUD with Mysql database.

## To Deploy in Ubuntu, Gunicorn and Apache2 server:

* Clone the project:
`git clone https://github.com/ferralespereira/WebFlask.git`

* Go to project folder and create a venv (virtual enviroment):
`python3 -m venv venv`

* Activate venv:
`source venv/bin/activate`

* Install flask and this others package into venv:
`pip3 install flask; pip3 install wtforms`

* Install Gunicorn:
`pip3 install gunicorn`

* Create a "wsgi.py" file into your folder root like this:
```
from main import app

if __name__ == '__main__':
    app.run() 

```

* Run gunicorn (to try if everything is working good so far):
`gunicorn --bind 127.0.0.1:8080 wsgi:app`

* Deactivate virtual enviroment:
`deactivate`

### ----------*Second Part of Deploiment*------------

* Create a file named "gunicorn_config.py" like this in the root of your project folder:
```
import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
bind = 'unix:webflask.sock'
umask = 0o007
reload = True

#logging
accesslog = '-'
errorlog = '-'
```

* Create systemd Unit File (to allow Ubuntu’s init system to automatically start Gunicorn and serve Flask application whenever the server or your computer restarts:
`sudo nano /etc/systemd/system/webflask.service`
* Write this inside:
```
[Unit]
Description=Gunicorn instance to serve web-flask
After=network.target

[Service]
User=root
Group=www-data
WorkingDirectory=/var/www/html/web-flask
Environment="PATH=/var/www/html/web-flask/venv/bin"
ExecStart=/var/www/html/web-flask/venv/bin/gunicorn --config gunicorn_config.py wsgi:app

[Install]
WantedBy=multi-user.target
```

* Start and Enable the new service:
`sudo systemctl start webflask.service; sudo systemctl enable webflask.service`

* Reload, Restart and Status ststemctl:
`sudo systemctl daemon-reload; sudo systemctl restart webflask.service; sudo systemctl status webflask.service`
