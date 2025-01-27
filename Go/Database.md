# Database

- Start PostgreSQL service
```bash
sudo service postgresql start
```

- Set up a password for postgres user
```bash
# Switch to postgres user
sudo -i -u postgres

# Access PostgreSQL prompt
psql

# Set password for postgres user
\password postgres

# Create your user (replace 'alisheikhattar' with your username)
CREATE USER alisheikhattar WITH PASSWORD 'your_password';

# Grant necessary privileges
ALTER USER alisheikhattar WITH SUPERUSER;
```

- connect
```bash
psql -U alisheikhattar
# or
psql -U alisheikhattar -d postgres
```

- after changes
```bash
sudo service postgresql restart
```

- connect to postgre
```bash
psql -U postgres
```

- connect through system account
```bash
# Switch to postgres system user
sudo -i -u postgres

# Then access psql
psql
```

- cli commands
```sql
-- List all databases
\l

-- Connect to a database
\c database_name

-- List all tables in current database
\dt

-- List all users
\du

-- Describe a table
\d table_name

-- Exit PostgreSQL CLI
\q
```

- Create table
```sql
CREATE DATABASE <recordings>;
```

- switches your current working database to “recordings”
```sql
\c recordings
-- or
\connect recordings
```

- list all databases
```sql
\l
```

- verify the current database
```sql
SELECT current_database();
-- or
\conninfo
```

- List tables in current database
```sql
\dt
```

- Execute sql file 
```sql
\i </home/asa/Code/Go_Tutorial/lssn3-database/create-tables.sql>
```

- Check table permissions
```sql
\z album
```

- Grant permissions to user:
```sql
GRANT ALL PRIVILEGES ON TABLE <album> TO <your_username>;
```

- Grant permission for retrieving id
```sql
GRANT USAGE, SELECT ON SEQUENCE <album>_id_seq TO <your_username>;
```
