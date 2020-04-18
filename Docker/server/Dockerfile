FROM python:3.7

COPY . /usr/src/app

RUN pip install --upgrade pip && \ 
pip install pipenv && \
pipenv lock && \
pipenv install --system --deploy --ignore-pipfile

WORKDIR /usr/src/app/src/api

CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]