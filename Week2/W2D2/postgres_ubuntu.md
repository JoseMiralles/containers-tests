# Postgresql in Ubuntu

This will create a new linux user `postgres`, which can access the database.

# Installation

- Install: `sudo apt install postgresql`

<br>

# Using PostgreSQL

1. Start: `sudo systemctl start postgresql.service`
1. In a new terminal, switch to the postgres user: `sudo -i -u postgres`
1. Access PostgreSQL `psql`
    - Without switching accounts: `sudo -u postgres psql`

More: https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04
