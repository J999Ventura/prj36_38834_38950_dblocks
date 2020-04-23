FROM python:3.7

COPY . /usr/src/app

WORKDIR /usr/src/app/src/api

RUN pip install --upgrade pip && \
    pip install pipenv && \
	pipenv lock && \
    pipenv install --dev --system --deploy --ignore-pipfile


#CMD gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:455 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info --reload
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]