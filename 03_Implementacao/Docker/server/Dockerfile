FROM python:3.7

ENV FLASK_ENV=production
ENV SECRET_KEY=b'\xcb\xd8\x15\xd9\xf1\x94R\xbd\x8b\xdfsv\xe7{\x9b\x08'
ENV MAIL_USERNAME=betamain10@gmail.com
ENV MAIL_PASSWORD=alphamain_10
ENV PRAETORIAN_CONFIRMATION_SENDER=betamain10@gmail.com
ENV PRAETORIAN_RESET_SENDER=betamain10@gmail.com
ENV PRAETORIAN_RESET_URI=http://localhost:8000/api/v1/auth/completeresetpwd
ENV SQLALCHEMY_DATABASE_URI=postgres://postgres:captureadm@35.187.10.224:5432/capturedb
ENV MAIL_SERVER=smtp.googlemail.com
ENV MAIL_PORT=587
ENV MAIL_USE_TLS=True
ENV PRAETORIAN_CONFIRMATION_SUBJECT=UserRegistration
ENV PRAETORIAN_CONFIRMATION_URI=http://localhost:8000/api/v1/auth/verify
ENV JWT_ACCESS_LIFESPAN=24hours
ENV JWT_REFRESH_LIFESPAN=2days

COPY . /usr/src/app
WORKDIR /usr/src/app/src

RUN pip install --upgrade pip && \
	pip install -r requirements.txt


CMD gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:8080 wsgi:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info --reload
#CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]