
# Account Response

*This model accepts additional fields of type Any.*

## Structure

`AccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Required | Identifier of an taxabilityType – as described in the request payload |
| `trades` | [`List[Trade]`](../../doc/models/trade.md) | Required | Trades for current date - “today” & end of the current year – “endOfCurrentYear”<br>                    Note: <br>                    On current date, the trade type will always be “rebalancing” – if the portfolio is changed. <br>                    For end of the year, the trade type will always be “withdrawal” |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
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
```

