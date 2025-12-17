
# Sub Merchants Get Response

## Structure

`SubMerchantsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `sub_merchant` | [`SubMerchant`](../../doc/models/sub-merchant.md) | Optional | - |
| `terminals` | [`List[Terminal]`](../../doc/models/terminal.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage6",
  "subMerchant": {
    "id": 254,
    "mid": 210,
    "uuid": "0000190c-0000-0000-0000-000000000000",
    "chainCode": "chainCode8",
    "divisionCode": "divisionCode6",
    "storeNumber": "storeNumber0",
    "federalTaxId": "federalTaxId4",
    "legalName": "legalName2",
    "dbaName": "dbaName4",
    "billingDescriptor": "billingDescriptor6",
    "ownershipType": "SoleProprietorship",
    "businessType": "Lodging",
    "mccCode": "mccCode4",
    "businessEstablishedDate": "2016-03-13",
    "transactionType": "OnlineStore",
    "websiteUrl": "websiteUrl4",
    "contacts": [
      {
        "title": "title4",
        "firstName": "firstName6",
        "middleInitial": "middleInitial6",
        "lastName": "lastName2",
        "phoneNumber": "phoneNumber2",
        "phoneNumberExt": "phoneNumberExt8",
        "email": "email8",
        "faxNumber": "faxNumber2",
        "type": "Primary"
      },
      {
        "title": "title4",
        "firstName": "firstName6",
        "middleInitial": "middleInitial6",
        "lastName": "lastName2",
        "phoneNumber": "phoneNumber2",
        "phoneNumberExt": "phoneNumberExt8",
        "email": "email8",
        "faxNumber": "faxNumber2",
        "type": "Primary"
      },
      {
        "title": "title4",
        "firstName": "firstName6",
        "middleInitial": "middleInitial6",
        "lastName": "lastName2",
        "phoneNumber": "phoneNumber2",
        "phoneNumberExt": "phoneNumberExt8",
        "email": "email8",
        "faxNumber": "faxNumber2",
        "type": "Primary"
      }
    ],
    "addresses": [
      {
        "addressLine1": "addressLine16",
        "addressLine2": "addressLine24",
        "city": "city4",
        "state": "GA",
        "country": "US",
        "postalCode": "postalCode4",
        "postalCodeExtension": "postalCodeExtension2",
        "type": "Mailing"
      },
      {
        "addressLine1": "addressLine16",
        "addressLine2": "addressLine24",
        "city": "city4",
        "state": "GA",
        "country": "US",
        "postalCode": "postalCode4",
        "postalCodeExtension": "postalCodeExtension2",
        "type": "Mailing"
      },
      {
        "addressLine1": "addressLine16",
        "addressLine2": "addressLine24",
        "city": "city4",
        "state": "GA",
        "country": "US",
        "postalCode": "postalCode4",
        "postalCodeExtension": "postalCodeExtension2",
        "type": "Mailing"
      }
    ],
    "acceptedCards": [
      {
        "attributes": [
          {
            "name": "name4",
            "value": "value6"
          },
          {
            "name": "name4",
            "value": "value6"
          },
          {
            "name": "name4",
            "value": "value6"
          }
        ],
        "type": "FleetCor"
      }
    ],
    "defaultBankAccount": {
      "ddaType": "Checking",
      "achType": "CommercialChequing",
      "accountNumber": "accountNumber8",
      "routingNumber": "routingNumber2"
    }
  },
  "terminals": [
    {
      "id": "id4",
      "tid": "tid4",
      "model": "model2",
      "frontEnd": "frontEnd4",
      "environment": "environment0"
    }
  ]
}
```

