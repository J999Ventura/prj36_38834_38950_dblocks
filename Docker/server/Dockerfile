FROM python:3-onbuild

COPY . /usr/src/app

RUN pip install --upgrade pip && \ 
pip install pipenv && \
cd src/api && \
pipenv install && \
pipenv shell && \
cd ../..

#CMD ["python", "flask db init && flask db migrate -m "Initial migration." && flask db upgrade"]
CMD ["python", "src/api/app.py"]