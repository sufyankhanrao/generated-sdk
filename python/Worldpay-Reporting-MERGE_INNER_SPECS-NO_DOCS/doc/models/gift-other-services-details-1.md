
# Gift Other Services Details 1

Other service details of gift card transaction.

## Structure

`GiftOtherServicesDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `stand_in_indicator` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Indicates standin option is available or not. |
| `stand_in_level` | [`CodeAndDescription4`](../../doc/models/code-and-description-4.md) | Optional | Standin level details. |

## Example (as JSON)

```json
{
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
```

