
# Response Transaction Level 3 Visa

## Structure

`ResponseTransactionLevel3Visa`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type96Enum`](../../doc/models/type-96-enum.md) | Optional | Resource Type<br><br>**Default**: `"TransactionLevel3Visa"` |
| `data` | [`Data24`](../../doc/models/data-24.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "TransactionLevel3Visa",
  "data": {
    "id": "id0",
    "transaction_id": "transaction_id8",
    "level3_data": {
      "destination_country_code": "destination_country_code4",
      "duty_amount": 182,
      "freight_amount": 60,
      "national_tax": 999999998999,
      "sales_tax": 999999998999
    }
  }
}
```

