
# Gift Additional Details

Additional details of gift transaction.

## Structure

`GiftAdditionalDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `call_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field indicates the type of call for authorization. |
| `gc_retrieval_reference_number` | `str` | Optional | Gift Card Retrieval Reference Number, a key to uniquely identify a card transaction based on the ISO 8583 standard. Appears for gift<br><br>**Constraints**: *Maximum Length*: `12` |
| `card_accountt_term` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Card account term details. |
| `merchant_category` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. |

## Example (as JSON)

```json
{
  "merchantCategory": {
    "code": "5812",
    "shortDescription": "RESTAURANTS",
    "longDescription": "EATING PLACES AND RESTAURANTS"
  },
  "callType": {
    "code": "code4",
    "shortDescription": "shortDescription8",
    "longDescription": "longDescription6"
  },
  "gcRetrievalReferenceNumber": "gcRetrievalReferenceNumber6",
  "cardAccounttTerm": {
    "code": "code6",
    "shortDescription": "shortDescription6",
    "longDescription": "longDescription8"
  }
}
```

