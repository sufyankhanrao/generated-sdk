
# Debit Transaction Details Response

Search results for debit card transaction details.

## Structure

`DebitTransactionDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_details` | [`DebitTransactionDetails`](../../doc/models/debit-transaction-details.md) | Optional | Authorization details of debit transaction. |
| `card_details` | [`DebitCardDetails`](../../doc/models/debit-card-details.md) | Optional | Debit card details. |
| `location_details` | [`DebitMerchantHierarchyDetails`](../../doc/models/debit-merchant-hierarchy-details.md) | Optional | Location details. |
| `petro_details` | [`DebitPetroDetails`](../../doc/models/debit-petro-details.md) | Optional | Petro details. |
| `fraud_sight` | [`DebitFraudSightDetails`](../../doc/models/debit-fraud-sight-details.md) | Optional | Fraud sight details. |
| `premium_payback` | [`DebitPremiumPaybackDetails`](../../doc/models/debit-premium-payback-details.md) | Optional | Premium payback details. |
| `other_services` | [`DebitOtherServicesDetails`](../../doc/models/debit-other-services-details.md) | Optional | Other service details. |

## Example (as JSON)

```json
{
  "transactionDetails": {
    "transactionId": "transactionId4",
    "transactionDateTime": "transactionDateTime8",
    "transactionProcessDate": "transactionProcessDate8",
    "transactionType": null,
    "denialCode": null
  },
  "cardDetails": {
    "cardNetwork": null,
    "token": "token2",
    "tokenId": "tokenId6",
    "tokenRequestorId": "tokenRequestorId0",
    "tokenAssuranceLevel": "tokenAssuranceLevel8"
  },
  "locationDetails": {
    "acro": "acro2",
    "chainCode": "chainCode2",
    "divisionNumber": "divisionNumber2",
    "storeNumber": "storeNumber6",
    "merchantId": "merchantId8"
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

