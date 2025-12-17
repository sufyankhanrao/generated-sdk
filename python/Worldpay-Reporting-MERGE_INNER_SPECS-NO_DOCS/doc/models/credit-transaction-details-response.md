
# Credit Transaction Details Response

Search results for credit card transaction details.

## Structure

`CreditTransactionDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_details` | [`TransactionDetails`](../../doc/models/transaction-details.md) | Optional | Authorization details for credit transaction. |
| `card_details` | [`CardDetails`](../../doc/models/card-details.md) | Optional | Credit card details. |
| `location_details` | [`MerchantHierarchyDetails`](../../doc/models/merchant-hierarchy-details.md) | Optional | Location details. |
| `petro_details` | [`PetroDetails`](../../doc/models/petro-details.md) | Optional | Petro details. |
| `fraud_sight` | [`FraudSightDetails`](../../doc/models/fraud-sight-details.md) | Optional | Fraud sight details. |
| `premium_payback` | [`PremiumPaybackDetails`](../../doc/models/premium-payback-details.md) | Optional | Premium payback details. |
| `other_services` | [`OtherServicesDetails`](../../doc/models/other-services-details.md) | Optional | Other service details |
| `additional_details` | [`AdditionalDetails`](../../doc/models/additional-details.md) | Optional | Additional details of the transaction. |

## Example (as JSON)

```json
{
  "authorizationDetails": {
    "transactionId": "transactionId8",
    "transactionDateTime": "transactionDateTime2",
    "transactionType": null,
    "transactionStatus": null,
    "entryMode": null
  },
  "cardDetails": {
    "cardNetwork": null,
    "cardHolderId": null,
    "cardAccountTerm": {
      "code": "code4",
      "shortDescription": "shortDescription8",
      "longDescription": "longDescription6"
    },
    "cardProductResults": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    },
    "cardEMV": false
  },
  "locationDetails": {
    "chainCode": "chainCode2",
    "divisionNumber": "divisionNumber2",
    "storeNumber": "storeNumber6",
    "merchantId": "merchantId8",
    "merchantName": "merchantName2"
  },
  "petroDetails": {
    "vehicleId": "vehicleId4",
    "driverId": "driverId0",
    "odometer": "odometer8",
    "poNumber": "poNumber6",
    "driverNumber": "driverNumber4"
  },
  "fraudSight": {
    "fraudScore": 20.16,
    "fraudRule": "fraudRule8",
    "fraudResponseCode": {
      "code": "code6",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription8"
    },
    "fraudRuleResult": {
      "code": "code2",
      "shortDescription": "shortDescription0",
      "longDescription": "longDescription4"
    },
    "fraudResponseTime": "2016-03-13T12:52:32.123Z"
  }
}
```

