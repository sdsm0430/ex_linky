# ex_linky

## setup
* sudo apt-get install python3-pip python3-dev libpq-dev postgresql postgresql-contrib nginx
* pip install django==1.11.10 gunicorn psycopg2

### [참고자료](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)
### psql
* sudo -u postgres psql
* CREATE DATABASE myproject;
* CREATE USER linkey WITH PASSWORD 'fldzl9397!';
```
ALTER ROLE linkey SET client_encoding TO 'utf8';
ALTER ROLE linkey SET default_transaction_isolation TO 'read committed';
ALTER ROLE linkey SET timezone TO 'UTC';
```
```
GRANT ALL PRIVILEGES ON DATABASE myproject TO linkey;
```
