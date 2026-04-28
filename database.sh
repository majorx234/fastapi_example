su -l postgres -c "initdb --locale=C.UTF-8 --encoding=UTF8 -D '/var/lib/postgres/data'"
systemctl start postgresql.service 
su - postgres -c "psql"
create user dbuser WITH PASSWORD '12345';
create database testdb owner dbuser;
GRANT ALL PRIVILEGES ON DATABASE "testdb" to dbuser;


psql -d testdb -c "\copy ratings FROM ratings_data.csv delimiter ',' CSV HEADER;"


or
\c testdb dbuser
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    birth_date DATE NOT NULL
);

INSERT INTO users (name, email, birth_date)
VALUES
    ('Alice Smith', 'alice@example.com', '1990-05-10'),
    ('Bob Miller', 'bob@example.com', '1985-11-23');

or 
\copy users FROM '/path/to/user_data.csv' delimiter ',' CSV HEADER;

