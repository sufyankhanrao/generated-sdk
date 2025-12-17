
# Gift Transaction Details Response

Search results for gift card transaction details.

## Structure

`GiftTransactionDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_details` | [`GiftTransactionDetails`](../../doc/models/gift-transaction-details.md) | Optional | Authorization details of gift card transaction. |
| `card_details` | [`GiftCardDetails`](../../doc/models/gift-card-details.md) | Optional | Gift card details. |
| `location_details` | [`GiftMerchantHierarchyDetails`](../../doc/models/gift-merchant-hierarchy-details.md) | Optional | Location details. |
| `fraud_sight` | [`GiftFraudSightDetails`](../../doc/models/gift-fraud-sight-details.md) | Optional | Fraud sight details. |
| `other_services` | [`GiftOtherServicesDetails`](../../doc/models/gift-other-services-details.md) | Optional | Other service details. |
| `additional_details` | [`GiftAdditionalDetails`](../../doc/models/gift-additional-details.md) | Optional | Additional details of gift card transaction. |

## Example (as JSON)

```json
{
  "transactionDetails": {
    "transactionId": "transactionId4",
    "transactionDateTime": "transactionDateTime8",
    "businessDate": "businessDate6",
    "transactionType": null,
    "entryMode": null
  },
  "cardDetails": {
    "cardNetwork": null,
    "cvv2ResponseCode": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    },
    "cvv2PresenceIndicator": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    },
    "token": "token2",
    "tokenId": "tokenId6"
  },
  "locationDetails": {
    "chainCode": "chainCode2",
    "divisionNumber": "divisionNumber2",
    "storeNumber": "storeNumber6",
    "merchantId": "merchantId8",
    "merchantName": "merchantName2"
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
  },
  "otherServices": {
    "standInIndicator": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    },
    "standInLevel": {
      "code": "code6",
      "shortDescription": "shortDescription6",
      "longDescription": "longDescription8"
    }
  }
}
```

