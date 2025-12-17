
# Equity Grant

*This model accepts additional fields of type Any.*

## Structure

`EquityGrant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_id` | `str` | Optional | Unique identifier of grant |
| `grant_date` | `datetime` | Optional | Date grant was given |
| `grant_type` | `str` | Optional | Type of grant |
| `seq_num` | `float` | Optional | - |
| `grant_price` | `float` | Optional | Grant price |
| `grant_currency_code` | `str` | Optional | Indicates the currency of grant USD vs AUD vs EUR etc (for share awards, you will still get a USD) |
| `quantity_granted` | `float` | Optional | Number of options |
| `quantity_outstanding` | `float` | Optional | - |
| `expiration_date` | `datetime` | Optional | Date grant expires |
| `vestings` | [`List[Vesting]`](../../doc/models/vesting.md) | Optional | An array of equityGrant vestings. Provides the past, present, and future vesting schedule and percentages. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "grantId": "grantId0",
  "grantDate": "2016-03-13T12:52:32.123Z",
  "grantType": "grantType0",
  "seqNum": 140.54,
  "grantPrice": 234.06,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

