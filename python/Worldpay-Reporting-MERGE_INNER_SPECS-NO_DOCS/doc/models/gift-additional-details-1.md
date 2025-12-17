
# Gift Additional Details 1

This object provides additional details on the transaction

## Structure

`GiftAdditionalDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `agent_bank` | `str` | Optional | Agent Bank Information<br><br>**Constraints**: *Maximum Length*: `256` |
| `merchant_category` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities. |

## Example (as JSON)

```json
{
  "agentBank": "0000",
  "merchantCategory": {
    "code": "5812",
    "shortDescription": "RESTAURANTS",
    "longDescription": "EATING PLACES AND RESTAURANTS"
  }
}
```

