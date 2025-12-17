
# Proposed Trades Current Year 2

Details of trade as of today i.e., current date & end of the year

*This model accepts additional fields of type Any.*

## Structure

`ProposedTradesCurrentYear2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `end_of_current_year` | [`EndOfCurrentYear`](../../doc/models/end-of-current-year.md) | Required | - |
| `today` | [`Today`](../../doc/models/today.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "endOfCurrentYear": {
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
            "tradeType": null,
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
  },
  "today": {
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
            "tradeType": null,
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
  },
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

