
# Additional Details

Additional details.

## Structure

`AdditionalDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `call_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the type of call for authorization. |
| `merchant_category` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. |
| `card_product_results` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This fields refers to the results of card products. |
| `card_account_term` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This fields refers to the term set for card account. |
| `market_specific_data_indicator` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates market specific data. |
| `retrieval_reference_number` | `str` | Optional | Retrieval Reference Number, a key to uniquely identify a card transaction based on the ISO 8583 standard. Appears for Credit<br><br>**Constraints**: *Maximum Length*: `12` |
| `settlement_type` | `str` | Optional | This field indicates the type of settlement for transactions.<br><br>**Constraints**: *Maximum Length*: `1` |

## Example (as JSON)

```json
{
  "merchantCategory": {
    "code": "5812",
    "shortDescription": "RESTAURANTS",
    "longDescription": "EATING PLACES AND RESTAURANTS"
  },
  "retrievalReferenceNumber": "216712523926",
  "settlementType": "Y",
  "callType": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  },
  "cardProductResults": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  },
  "cardAccountTerm": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  },
  "marketSpecificDataIndicator": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  }
}
```

