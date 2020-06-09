# Xero Data API

This is an API to handle Oauth transactions with Xero API. Check out the project's [documentation](http://nikkomidoy.github.io/xero-data-api/).

# Usage

You can run the project by two options. Using the `runserver` or `Docker`

# Running in traditional runserver

Create virtual environment. You can use the basic [virtualenv](https://virtualenv.pypa.io/en/latest/)
but here I'm using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
```bash
mkvirtualenv <name> -p python3
```

Activate the virtual environment and install necessary python packages.
```bash
pip install -r requirements.txt
```

Run migrations. By default, it runs over SQLite
```bash
python manage.py migrate
```

Run the local server
```bash
python manage.py runserver
```

# Running in Docker
## Prerequisites

- [Docker](https://docs.docker.com/docker-for-mac/install/)  

## Initial build of Docker
```bash
docker-compose up --build
```

## Local Development

Start the dev server for local development:
```bash
docker-compose up
```

Run a command inside the docker container:

```bash
docker-compose run --rm web [command]
```

# Accessability

API is available upon running either way at this link: `http://127.0.0.1:8000/api/v1/`

# Admin access

After running series of setup which includes migrations, you will have a default admin access as follows:
```
username: admin
email: admin@admin.com
password: adminpassword
```

