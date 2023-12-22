#  Management Dashboard
management dashboard for bottled water company

##  Setup
  This project uses [nx](https://nx.dev/) to manage project tasks. While nx
  itself is not a prerequisite (it is however, a dev-dependency), node and
  npm are. It's recommended to use node version manager such as
  [nvm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#using-a-node-version-manager-to-install-nodejs-and-npm)
  to manage node and npm versions. Installation and usage information can be
  found [here](https://github.com/nvm-sh/nvm?tab=readme-ov-file#installing-and-updating).

  The back-end is a [Django](https://www.djangoproject.com/) project with a
  [Django REST Framework](https://www.django-rest-framework.org/) api app.
  Again, Django and django-rest-framework are not prerequisite, but python
  is. It is recommended to use pyenv to manage python versions. Installation
  instructions can be found [here](https://realpython.com/intro-to-pyenv/#why-use-pyenv). 

  It is also recommended to use a virtual environment to isolate python
  package versions,
  [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
  provides a great set of tools for setting up and managing virtual
  environments.

### Frontend
  Follow the instructions above to set up a Node/JavaScript development
  environment. Then install the node dependencies **(make sure you are in
  the directory containing the `package.json` file)**.
  ```sh
  $ npm install
  ```
  Running a frontend development server is very simple, simply type the
  following in a terminal:
  ```sh
  $ npx nx run serve-fe
  ```
  This will spin up a development server for the front-end app. This will
  not start a server for the back-end app (see the next section).

### Backend
  Follow the instructions above to set up a python development environment.
  Then create a new virtual environment:
  ```sh
  $ mkvirtualenv management-dashboard
  ```
  You can exit the virtual environment by typing the following into the
  shell:
  ```sh
  $ deactivate
  ```
  To re-enter the virtual environment, type:
  ```sh
  $ workon management-dashboard
  ```
  Once in a fresh virtual environment, install project dependencies.
  Dependencies are divided into three requirements file
  `requirements-prod.txt`, `requirements-tests.txt` and
  `requirements-dev.txt`. Each subsequent file builds on the requirements
  in the preceding file.
  ```sh
  (management-dashboard)$ pip install -r requirements-dev.txt
  ```
  To serve the back-end app, a node development environment must be present
  and the JavaScript dependencies must be installed (see instructions above).
  ```sh
  (management-dashboard)$ npx nx run serve-be
  ```
  This will build the front-end app, place the files in a place where the
  django server can find them, make and run migrations, then spin up a
  development server. After some setup, the app can be viewed by visiting
  `127.0.0.1:8000/app`  and `127.0.0.1:8000/api`.

##  Tests
###  End-To-End
  The end-to-end tests are a set of
  [pytest](https://docs.pytest.org/en/7.4.x/contents.html)
  [selenium](https://selenium-python.readthedocs.io/index.html) tests. To
  setup, run and develop the end-to-end tests you must first setup a python
  development environment, install the dependencies, serve the application,
  then run the tests. Follow the instructions under "backend setup",  after
  switching into your virtual environment and installing the test
  dependencies you need to serve the application. Finally change into the
  `tests` directory, and run the tests:
  ```sh
  (management-dashboard)$ python -m pytest
  ```

## App Deployment
### Environment
  In addition to the environment variables defined by the python system and
  the Django framework, This app makes use of the following additional
  environment variables:
  1. `DEVELOPMENT`: used to determine whether the app is in development,
     testing, or production mode. Accepted values are `development`,
     `production` or `testing`.
  2. `PROJECT_ROOT`: the path to the projects root directory.
  3. `FLY_APP_NAME`: this is a value set by the fly.io server. This is
     only used in production mode.
  4. `SECRET_KEY`: the django secret key

  When the `DEVELOPMENT` environment variable is set to 'development', the
  following takes place in `settings.py`:
  1. `SECRET_KEY` is set to a rondom hardcoded value just to ensure that the
     key is not empty (which would cause an error).
  2. `ALLOWED_HOSTS` is set to an empty list.
  3. `DEBUG` is set to `True`.

  When `DEVELOPMENT` environment variable is set to 'production', the
  following takes place in `settings.py`:
  1. `SECRET_KEY` is set to the value of the `SECRET_KEY` environment
     variable. Note that if the environment variable is not set the app will
     not work.
  2. `ALLOWED_HOSTS` value in `settings.py` is set to a list containing the
     domain name of the app server. Note that if the `FLY_APP_NAME`
     environment variable is unset the app will not work.
  3. `DEBUG` is set to `False`.
  4. `CSRF_COOKIE_SECURE` and `SESSION_COOKIE_SECURE` are set to `True`.

### Deployment Process
  To deploy this app:
  1. install the front-end dependencies
     ```sh
     $ npm install
     ```
  2. build the front-end app
     ```sh
     $ npx nx build
     ```
     this will build the front-end app and place the artifacts in
     '<project root>/static/build'.
  3. copy the '<project root>/src/app/api' directory to a new 'app root'
    ```sh
    $ cp -r src/app/api <deploy root>/
    ```
  4. copy the '<project root>/src/app/djang_project_root' directory to new
     'app root'
     ```sh
    $ cp -r src/app/django_project_root <deploy root>/
     ```
  2. install backend dependencies
    ```sh
    (management-dashboard)$ pip install -r requirements-prod.txt
    ```
  6. collect static files
    ```sh
    (management-dashboard)$ npx nx collect-static
    ```
  7. make and apply migrations
    ```sh
    (management-dashboard)$ npx nx makemigrations
    (management-dashboard)$ npx nx migrate
    ```
  The app is now ready to be deployed using your prefered server. You can
  use gunicorn to serve the app by running the following command from the
  deployment root directory.
  ```sh
  (management-dashboard)$ gunicorn django_project_root.wsgi
  ```
### Docker
  The deployment process above is encoded into a two-stage docker build.
  The first stage sets up and builds the front-end app. The second stage
  copies files needed to run the app into the appropriate directories,
  makes and apply migrations and runs a gunicorn server that listends on
  port 80. To build the docker image run the following command:
  ```sh
  $ docker build -f Dockerfile --build-arg="development=development" \
    --target=stage-two -t dashboard .
  ```
  This will build the image with the `DEVELOPMENT` environment variable
  set to 'development'. To run the image:
  ```sh
  $ docker run -p 8080:80 --name="dashboard-i" -itd dashboard
  ```
