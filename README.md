# kwanso-demo

## How to setup the project

- first install python on your PC
- Once you have python, then open a terminal in the root of the project and execute the following command

``` bash
python -m venv venv
```

- For PC

```bash
source venv\Scripts\activate
```

- For Mac / Linux

```bash
source venv/bin/activate
```

- After that, run the following command to install project requirements

```bash
pip install wheel
pip install -r requirements.txt
```

- Once the requirements are installed, then run the below commands

```bash
python manage.py makemigrations
python manage.py migrate
python runserver
```

- Once the project runs and the webserver starts, the following links can be used on the API

- [POST http://localhost:8000/register/](http://localhost:8000/register/)
- [POST http://localhost:8000/login/](http://localhost:8000/login/)
- [GET http://localhost:8000/user/](http://localhost:8000/user/)
- [POST http://localhost:8000/create-task/](http://localhost:8000/create-task/)
- [GET http://localhost:8000/list-task/](http://localhost:8000/list-task/)
