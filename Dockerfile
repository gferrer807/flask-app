FROM python:3.11-alpine
WORKDIR /usr/src/backend
RUN pip install pipenv
COPY Pipfile* ./
RUN pipenv install
COPY . /usr/src/backend
EXPOSE 5000
CMD pipenv run gunicorn app:app -c docker-gunicorn.conf.py
