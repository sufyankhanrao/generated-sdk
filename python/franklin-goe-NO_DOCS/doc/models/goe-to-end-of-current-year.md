
# Goe to End of Current Year

*This model accepts additional fields of type Any.*

## Structure

`GoeToEndOfCurrentYear`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accounts` | [`List[GoeToAccountResponse]`](../../doc/models/goe-to-account-response.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accounts": [
    {
      "accountID": "T",
      "trades": [
        {
          "direction": "S",
          "symbol": "CASH",
          "cusip": "cusip4",
          "quantity": 29178.0,
          "amount": 10748.399065,
          "phase": "phase2",
          "exampleAdditionalProperty": {
            "key1": "val1",
            "key2": "val2"
          }
        }
      ],
      "exampleAdditionalProperty": {
        "key1": "val1",
        "key2": "val2"
      }
    }
  ],
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

