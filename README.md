# management-dashboard
management dashboard for bottled water company

## Setup

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages management-dashboard
$ source management-dashboard/bin/activate
```

Then install the dependencies:

```sh
(management-dashboard)$ pip install -r requirements.txt
```
Note the `(management-dashboard)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(management-dashboard)$ cd project
(management-dashboard)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000`.
