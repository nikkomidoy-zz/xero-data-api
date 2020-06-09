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

# Setting up Xero developers account

You can follow this [guidelines](https://developer.xero.com/documentation/getting-started/getting-started-guide)
in creating a developers app in Xero account.

Upon creating your developer apps, make sure that your
callback uri will be: ``http://localhost:8000/api/v1/xero/process/callback/``

This allows to process the connection to Xero API after the user
authorizes the app.


# Google sheet

I'll be sharing the spreadsheet in which bank transactions being recorded.

# All about Xero
API documentation in all about Xero transactions

## Authorize to Xero account

**Request**:

`GET` `/api/v1/xero/login/?client_id=<client-id>&client_secret=<client-secret>`

Parameters:
Parameters:

Name         | Type   | Description
-------------|--------|---
client_id    | string | Client id from Xero developer app
client_secret| string | Client secret from Xero developer app



*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```.env
Redirected to Xero App for App Authorization
```

## Get all bank transactions in Xero

**Request**:

`GET` `/api/v1/bank/transactions/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "BankTransactionID": "b9d7c42c-506a-4e56-a8a1-a41330580834",
        "BankAccount": {
            "AccountID": "562555f2-8cde-4ce9-8203-0363922537a4",
            "Code": "090",
            "Name": "Business Bank Account"
        },
        "Type": "SPEND",
        "Reference": "Fee",
        "IsReconciled": true,
        "HasAttachments": false,
        "Contact": {
            "ContactID": "43d1337e-4360-4589-9a76-1d0538c4ce6f",
            "Name": "Ridgeway Bank",
            "Addresses": [],
            "Phones": [],
            "ContactGroups": [],
            "ContactPersons": [],
            "HasValidationErrors": false
        },
        "DateString": "2020-03-28",
        "Date": "2020-03-28T00:00:00",
        "Status": "AUTHORISED",
        "LineAmountTypes": "Inclusive",
        "LineItems": [],
        "SubTotal": 15.0,
        "TotalTax": 0.0,
        "Total": 15.0,
        "UpdatedDateUTC": "2008-12-20T22:50:55.090000",
        "CurrencyCode": "USD"
    }
]
```


## Post all bank transactions in Google sheet

**Request**:

`GET` `/api/v1/bank/transactions/spreadsheet/`

Parameters:

*Note:*

- **[Authorization Protected](authentication.md)**

**Response**:

```json
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "Success": "You have successfully posted bank transactions to socameras-test spreadsheet"
}
```

### Important note: All endpoints are authenticated. You can login using the [browesable API](http://127.0.0.1:8000/api-auth/login/).
