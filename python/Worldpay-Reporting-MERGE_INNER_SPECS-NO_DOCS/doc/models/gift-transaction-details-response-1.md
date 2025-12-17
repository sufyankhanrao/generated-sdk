
# Gift Transaction Details Response 1

This object provides the details of the gift transactions

## Structure

`GiftTransactionDetailsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_details` | [`GiftTransactionDetails1`](../../doc/models/gift-transaction-details-1.md) | Optional | Resource is used for transaction details |
| `card_details` | [`GiftCardDetails1`](../../doc/models/gift-card-details-1.md) | Optional | This object provides credit card related information |
| `location_details` | [`GiftMerchantHierarchyDetails1`](../../doc/models/gift-merchant-hierarchy-details-1.md) | Optional | This object provides details of transaction location -- merchant related information |
| `other_services` | [`GiftOtherServicesDetails1`](../../doc/models/gift-other-services-details-1.md) | Optional | Other service details. |
| `additional_details` | [`GiftAdditionalDetails1`](../../doc/models/gift-additional-details-1.md) | Optional | This object provides additional details on the transaction |

## Example (as JSON)

```json
{
  "transactionDetails": {
    "transactionId": "transactionId4",
    "processDate": "processDate4",
    "transactionDateTime": "transactionDateTime8",
    "transactionType": null,
    "authorizationCode": "authorizationCode2"
  },
  "cardDetails": {
    "cardNetwork": null,
    "token": "token2",
    "tokenId": "tokenId6",
    "cvv2ResponseCode": null,
    "cvv2PresenceIndicator": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    }
  },
  "locationDetails": {
    "storeNumber": "storeNumber6",
    "merchantId": "merchantId8",
    "alternateMerchantId": "alternateMerchantId8"
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
  },
  "additionalDetails": {
    "agentBank": "agentBank0",
    "merchantCategory": null
  }
}
```

