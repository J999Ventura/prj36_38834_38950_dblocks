"/bin/bash"
set PGUSER=postgres
psql
\connect capture
GRANT ALL PRIVILEGES ON DATABASE capture TO dbadmin;
CREATE SCHEMA IF NOT EXISTS CAPTURE_ADM AUTHORIZATION dbadmin;