
# Gift Real Transaction Details Response

Search results for gift card real time transaction details.

## Structure

`GiftRealTransactionDetailsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `authorization_details` | [`RealGiftTransactionDetails`](../../doc/models/real-gift-transaction-details.md) | Optional | Authorization details of real time gift card transaction. |
| `sensitive_gift_card_details` | [`SensitiveGiftRealCardDetails`](../../doc/models/sensitive-gift-real-card-details.md) | Optional | Sensitive card details |
| `card_details` | [`RealGiftCardDetails`](../../doc/models/real-gift-card-details.md) | Optional | Gift card details. |
| `location_details` | [`RealGiftMerchantHierarchyDetails`](../../doc/models/real-gift-merchant-hierarchy-details.md) | Optional | Location details. |
| `fraud_sight` | [`RealGiftFraudSightDetails`](../../doc/models/real-gift-fraud-sight-details.md) | Optional | Fraud sight details. |
| `other_services` | [`RealGiftOtherServicesDetails`](../../doc/models/real-gift-other-services-details.md) | Optional | Other service details. |
| `addition_details` | [`RealGiftAdditionalDetails`](../../doc/models/real-gift-additional-details.md) | Optional | Additional details of gift card transaction. |
| `customer_fields` | [`CustomerFields`](../../doc/models/customer-fields.md) | Optional | Customer fields details. |

## Example (as JSON)

```json
{
  "authorizationDetails": {
    "transactionId": "transactionId8",
    "transactionDateTime": "transactionDateTime2",
    "businessDate": "businessDate0",
    "transactionCode": {
      "code": "code8",
      "shortDescription": "shortDescription6",
      "longDescription": "longDescription0"
    },
    "entryMode": null
  },
  "sensitiveGiftCardDetails": {
    "cardNumber": "cardNumber0",
    "expirationDate": "expirationDate8",
    "lastFourOfPAN": "lastFourOfPAN4"
  },
  "cardDetails": {
    "cardNetwork": null,
    "cardHolderId": null,
    "cardHolderVerificationMethod": "cardHolderVerificationMethod6",
    "cardAccountTerm": {
      "code": "code4",
      "shortDescription": "shortDescription8",
      "longDescription": "longDescription6"
    },
    "cvv2ResponseCode": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    }
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
  }
}
```

