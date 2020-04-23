FROM postgres
COPY . /usr/src/app
ADD scripts/init_db.sql /docker-entrypoint-initdb.d/
