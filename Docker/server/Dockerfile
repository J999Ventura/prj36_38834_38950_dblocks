FROM python:3.7

COPY . /usr/src/app

WORKDIR /usr/src/app/src/api

RUN pip install --upgrade pip && \
    pip install pipenv && \
	pipenv lock && \
    pipenv install --dev --system --deploy --ignore-pipfile
	
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]