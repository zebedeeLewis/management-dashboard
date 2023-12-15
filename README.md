#  Management Dashboard
management dashboard for bottled water company

##  Setup
This project uses  [nx](https://nx.dev/) to manage project tasks. While nx itself is not a prerequisite (it is however, a dev-dependency), node and npm are. It's recommended to use node version manager such as [nvm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#using-a-node-version-manager-to-install-nodejs-and-npm) to manage node and npm versions. Installation and usage information can be found [here](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

The back-end is a [Django](https://www.djangoproject.com/) project with a [Django REST Framework](https://www.django-rest-framework.org/) api app. Again, Django and django-rest-framework are not prerequisite, but python is. It is recommended to use pyenv to manage python versions. Installation instructions can be found [here](https://realpython.com/intro-to-pyenv/#why-use-pyenv). 

It is also recommended to use a virtual environment to isolate python package versions, [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/) provides a great set of tools for setting up and managing virtual environments.

### Frontend
Follow the instructions above to set up a Node/JavaScript development environment. Then install the node dependencies **(make sure you are in the directory containing the `package.json` file)**.
```sh
$ npm install
```
Running a frontend development server is very simple, simply type the following in a terminal:
```sh
$ npx nx run serve-fe
```
This will spin up a development server for the front-end app. This will not start a server for the back-end app (see the next section).


### Backend
Follow the instructions above to set up a python development environment. Then create a new virtual environment:
```sh
$ mkvirtualenv management-dashboard
```
You can exit the virtual environment by typing the following into the shell:
```sh
$ deactivate
```
To re-enter the virtual environment, type:
```sh
$ workon management-dashboard
```
Once in a fresh virtual environment, install project dependencies.
Dependencies are divided into three requirements file `requirements-prod.txt`, `requirements-tests.txt` and `requirements-dev.txt`. Each subsequent file builds on the requirements in the preceding file.
```sh
(management-dashboard)$ pip install -r requirements-dev.txt
```
To serve the back-end app, a node development environment must be present and the JavaScript dependencies must be installed (see instructions above).
```sh
(management-dashboard)$ npx nx run serve-be
```
This will build the front-end app, place the files in a place where the django server can find them, make and run migrations, then spin up a development server. After some setup, the app can be viewed by visiting `127.0.0.1:8000/app`  and `127.0.0.1:8000/api`.


##  Tests
###  End-To-End
The end-to-end tests are a set of [pytest](https://docs.pytest.org/en/7.4.x/contents.html) [selenium](https://selenium-python.readthedocs.io/index.html) tests. To setup, run and develop the end-to-end tests you must first setup a python development environment, install the dependencies, serve the application, then run the tests. Follow the instructions under "backend setup",  after switching into your virtual environment and installing the test dependencies you need to serve the application. Finally change into the `tests` directory, and run the tests:
```sh
(management-dashboard)$ python -m pytest
```
