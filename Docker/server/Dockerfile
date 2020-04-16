FROM python:3.7

COPY . /usr/src/app
WORKDIR /usr/src/app/src/api

RUN pip install --upgrade pip && pip install pipenv && pipenv lock && pipenv install --system --deploy

RUN pipenv graph
RUN pipenv lock -r

#CMD ["pipenv", "lock", "-r"]
#CMD ["pipenv", "run", "python", "app.py"]