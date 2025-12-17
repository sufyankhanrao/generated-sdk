
# Credit Transaction Details Response 1

This object provides the details of the credit transactions

## Structure

`CreditTransactionDetailsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_details` | [`CreditTransactionDetails`](../../doc/models/credit-transaction-details.md) | Optional | This object provides transaction amount related information |
| `card_details` | [`CreditCardDetails`](../../doc/models/credit-card-details.md) | Optional | This object provides credit card related information |
| `location_details` | [`CreditMerchantHierarchyDetails`](../../doc/models/credit-merchant-hierarchy-details.md) | Optional | This object provides details of transaction location -- merchant related information |
| `inter_change_details` | [`CreditInterChangeDetails`](../../doc/models/credit-inter-change-details.md) | Optional | This object provides information on interchange related details |
| `premium_payback` | [`CreditPremiumPaybackDetails`](../../doc/models/credit-premium-payback-details.md) | Optional | This object provides information on payback related details |
| `other_services` | [`CreditOtherServicesDetails`](../../doc/models/credit-other-services-details.md) | Optional | This object provides information on other services related information. |
| `additional_details` | [`CreditAdditionalDetails`](../../doc/models/credit-additional-details.md) | Optional | This object provides additional details on the transaction |

## Example (as JSON)

```json
{
  "transactionDetails": {
    "transactionId": "transactionId4",
    "processDate": "processDate4",
    "transactionDateTime": "transactionDateTime8",
    "authorizationAmount": 190.72,
    "authorizationCode": 38
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
    "storeNumber": "storeNumber6",
    "merchantId": "merchantId8",
    "alternateMerchantId": "alternateMerchantId8",
    "merchantName": "merchantName2",
    "employeeNumber": 9
  },
  "interChangeDetails": {
    "cardProductResults": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    },
    "cardProductType": {
      "code": "code0",
      "shortDescription": "shortDescription2",
      "longDescription": "longDescription2"
    },
    "daysLate": "daysLate4",
    "discountAmount": "discountAmount0",
    "interchange": "interchange6"
  },
  "premiumPayback": {
    "indicatorPassed": false,
    "eligibleBIN": false,
    "eligible": false,
    "redemptionAccepted": false,
    "redemptionAmount": "redemptionAmount6"
  }
}
```

