#  Management Dashboard
management dashboard for bottled water company

##  Setup
### Back-end
The back-end portion of the application is a [Django](https://www.djangoproject.com/) project with a [Django REST Framework](https://www.django-rest-framework.org/) app (api). To setup, run and develop the back-end portion of this project you must first setup a python development environment, install the dependencies, then serve the development server.

Setup your python distribution. It's recommended to use pyenv to manage distributions. The installation steps can be found [here](https://realpython.com/intro-to-pyenv/#why-use-pyenv) . Once you've installed it, select a distribution and proceed.

Setup your virtual environment. The recommended way to do so is using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/), of course you could use whatever tool you prefer.

If you haven't setup a virtual environment for this porject:
```sh
$ pip install virtualenvwrapper
...
$ export WORKON_HOME=~/.venv
$ mkdir -p $WORKON_HOME
$ source /usr/local/bin/virtualenvwrapper.sh
$ mkvirtualenv management-dashboard
```
If you've already setup a virtual environment:
```sh
$ workon management-dashboard
```
This should put your shell in an isolated virtual environment where you could install the project dependencies.
```sh
(management-dashboard)$ pip install -r requirements-dev.txt
```
Now that all requirements are installed, you can start the development server. run the following command in the directory containing the `manage.py` file.
```sh
(management-dashboard)$ python manage.py runserver
```
###  Front-end
The front-end portion of the application is an [nx](https://nx.dev/) project with a [react](https://react.dev/) single page app. To setup, run and develop the front-end portion of this project you must first have npm installed, install the dependencies, then serve the development server.

Install dependencies. Run the following commands in the directory containing the `package.json` file.
```sh
$ npm install
```
Run the development server.
```sh
$ npx nx serve
```
