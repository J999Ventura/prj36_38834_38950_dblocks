FROM python:3-onbuild
COPY . /usr/src/app
RUN pip install --upgrade pip && pip install pipenv && pipenv install && pipenv shell && pipenv shell
CMD ["python", "flask db init && flask db migrate -m "Initial migration." && flask db upgrade"]
CMD ["python", "src/run.py"]