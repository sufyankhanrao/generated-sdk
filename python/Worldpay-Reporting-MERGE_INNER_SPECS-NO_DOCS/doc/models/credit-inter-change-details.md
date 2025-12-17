
# Credit Inter Change Details

This object provides information on interchange related details

## Structure

`CreditInterChangeDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_product_results` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Refers to card product results |
| `card_product_type` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Refers to card product |
| `days_late` | `str` | Optional | Number of days late<br><br>**Constraints**: *Maximum Length*: `256` |
| `discount_amount` | `str` | Optional | Discount Amount Value<br><br>**Constraints**: *Maximum Length*: `255` |
| `interchange` | `str` | Optional | Interchange details<br><br>**Constraints**: *Maximum Length*: `256` |
| `interchange_fees` | `str` | Optional | Interchange Fees<br><br>**Constraints**: *Maximum Length*: `255` |
| `organization_interchange_indicator` | `str` | Optional | Indicator of organization interchange.<br><br>**Constraints**: *Maximum Length*: `256` |
| `surcharge_amount` | `str` | Optional | Surcharge Amount<br><br>**Constraints**: *Maximum Length*: `255` |
| `surcharge_reason` | [`CodeAndDescription11`](../../doc/models/code-and-description-11.md) | Optional | Reason for Surcharge |
| `billing_indicator` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Refers to the bundling indicator for the Settled transaction. |

## Example (as JSON)

```json
{
  "daysLate": "02",
  "interchange": "000145253-VS DEBIT REGULATED",
  "interchangeFees": "17.25",
  "organizationInterchangeIndicator": "5",
  "surchargeAmount": "893.56",
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
  "discountAmount": "discountAmount8"
}
```

