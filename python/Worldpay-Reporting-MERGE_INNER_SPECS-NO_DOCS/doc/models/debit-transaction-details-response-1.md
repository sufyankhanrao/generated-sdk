
# Debit Transaction Details Response 1

This object provides the details of the debit transactions

## Structure

`DebitTransactionDetailsResponse1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_details` | [`DebitTransactionDetails1`](../../doc/models/debit-transaction-details-1.md) | Optional | This object provides transaction amount related information |
| `card_details` | [`DebitCardDetails1`](../../doc/models/debit-card-details-1.md) | Optional | This object provides card related information |
| `location_details` | [`DebitMerchantHierarchyDetails1`](../../doc/models/debit-merchant-hierarchy-details-1.md) | Optional | This object provides details of transaction location -- merchant related information |
| `premium_payback` | [`DebitPremiumPaybackDetails1`](../../doc/models/debit-premium-payback-details-1.md) | Optional | This object provides information on payback related details |
| `other_services` | [`DebitOtherServicesDetails1`](../../doc/models/debit-other-services-details-1.md) | Optional | Other service details. |
| `additional_details` | [`DebitAdditionalDetails`](../../doc/models/debit-additional-details.md) | Optional | This object provides additional details on the transaction |

## Example (as JSON)

```json
{
  "transactionDetails": {
    "transactionId": "transactionId4",
    "processDate": "processDate4",
    "transactionDateTime": "transactionDateTime8",
    "transactionType": null,
    "authorizationAmount": 190.72
  },
  "cardDetails": {
    "cardHolderBankAcro": "cardHolderBankAcro4",
    "token": "token2",
    "tokenId": "tokenId6",
    "tokenAssuranceLevel": "tokenAssuranceLevel8",
    "tokenExpirationDate": "tokenExpirationDate2"
  },
  "locationDetails": {
    "acro": "acro2",
    "chainCode": "chainCode2",
    "divisionNumber": "divisionNumber2",
    "storeNumber": "storeNumber6",
    "merchantId": "merchantId8"
  },
  "premiumPayback": {
    "indicatorPassed": false,
    "eligibleBIN": false,
    "eligible": false,
    "redemptionAccepted": false,
    "redemptionAmount": "redemptionAmount6"
  },
  "otherServices": {
    "standInIndicator": {
      "code": "code8",
      "shortDescription": "shortDescription4",
      "longDescription": "longDescription0"
    }
  }
}
```

