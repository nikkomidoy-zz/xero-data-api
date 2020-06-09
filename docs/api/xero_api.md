# All about Xero
API documentation in all about Xero transactions

## Authorize to Xero account

**Request**:

`GET` `/api/v1/xero/login/`

Parameters:

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
