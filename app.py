import psycopg2
from flask import Flask

app = Flask(__name__)

def connect_db():
    return psycopg2.connect(
        dbname = "mydb"
        user = "user"
        password = "password"
        host = "db"
    )

@app.rout("/")
def home():
    conn = connect_db()
    return "Connected to DB!"

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)

"""
Adding Docker-Compose
docker-compose is a separate binary which is best downloaded directly from the project's GitHub releases. Most popular Linux distributions do include Compose in their package managers but it can be significantly outdated.

Head to Docker Compose's releases page and take note of the latest version number. At the time of writing, it was 1.29.0.

Substitute the version you see instead of 1.29.0 in the command below. This will download the right binary for your system and drop it into /usr/local/bin.

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
Next make the file executable:

sudo chmod +x /usr/local/bin/docker-compose
You'll now be able to use the docker-compose command in your terminal. Try running docker-compose --version to check.
"""