
# Debit Additional Details

This object provides additional details on the transaction

## Structure

`DebitAdditionalDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pin_less` | `bool` | Optional | possible values True or False |
| `force_post` | `bool` | Optional | possible values True or False |
| `has_adjustment_records` | `str` | Optional | Refers to any adjustment made in records<br><br>**Constraints**: *Maximum Length*: `256` |
| `merchant_category` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. |

## Example (as JSON)

```json
{
  "pinLess": true,
  "forcePost": true,
  "hasAdjustmentRecords": "Not Adjusted",
  "merchantCategory": {
    "code": "5812",
    "shortDescription": "RESTAURANTS",
    "longDescription": "EATING PLACES AND RESTAURANTS"
  }
}
```

