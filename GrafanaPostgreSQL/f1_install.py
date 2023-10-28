import os

def grafana_init():
    pass
    # ::down grafana server by Terminal::
    os.chdir("/Users/ecpy/Documents")       # download to your /Documents
    os.system("curl -O https://dl.grafana.com/enterprise/release/grafana-enterprise-10.2.0.darwin-amd64.tar.gz")
    os.system("tar -zxvf grafana-enterprise-10.2.0.darwin-amd64.tar.gz")

    # ::start this server::
    os.chdir("/Users/ecpy/grafana")         # go into your grafana floder
    os.system("killall grafana")
    os.system("killall grafana-server")
    os.system("./bin/grafana-server start") # enable grafana and then you can access 127.0.0.1:3000 to get the grafana server in your Chrome (admin:admin)
    
    # os.system("./bin/grafana-server stop")
    # os.system("./bin/grafana-server restart")


def postgre_init():
    pass
    # ::down postgreSQL server by Chrome::
    # PostgreSQL.app: https://github.com/PostgresApp/PostgresApp/releases/download/v2.6.7/Postgres-2.6.7-16.dmg
    # pgAdmin.app   : https://ftp.postgresql.org/pub/pgadmin/pgadmin4/v7.8/macos/pgadmin4-7.8-arm64.dmg
    os.chdir("/Applications/Postgres.app/Contents/Versions/16")                                 # go into your postgres floder
    os.system('''./bin/psql -c "CREATE USER grafana WITH PASSWORD 'grafana';" ''')              # create user grafana:grafana
    os.system('''./bin/psql -c “CREATE DATABASE grafana_db OWNER grafana;"    ''')              # create user's database   (grafana_db)
    os.system('''./bin/psql -c "GRANT ALL PRIVILEGES ON DATABASE grafana_db to grafana;" ''')   # enable user's privileges (grafana_db)
    
    # os.system("./bin/psql -h 127.0.0.1 -d grafana_db -U grafana")       # connect postgres: you can run this command on your Terminal manually to get the postgres server

