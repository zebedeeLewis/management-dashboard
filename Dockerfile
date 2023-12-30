FROM node as stage-one

ENV NX_REJECT_UNKNOWN_LOCAL_CACHE=0 
WORKDIR /home/node/stage-one

COPY . .

RUN npm install
RUN npx nx build

FROM python:3 as stage-two

ARG run_mode=''
EXPOSE 80

ENV GUNICORN_CMD_ARGS="--bind=0.0.0.0:80 --workers=3"
ENV RUN_MODE=$run_mode

WORKDIR /usr/src/app

COPY src/app/api ./api
COPY src/app/django_project_root ./django_project_root
COPY --from=stage-one /home/node/stage-one/static/build static/build
COPY manage.py ./
COPY requirements-prod.txt ./

RUN pip install --no-cache-dir gunicorn
RUN pip install --no-cache-dir -r requirements-prod.txt
RUN python manage.py collectstatic
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN rm -rf static/build

CMD [ "gunicorn", "django_project_root.wsgi" ]
