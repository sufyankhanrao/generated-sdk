
# Payment Accelerater Detail

## Structure

`PaymentAcceleraterDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `status_code` | [`StatusCode1Enum`](../../doc/models/status-code-1-enum.md) | Optional | Payment Accelerator status code.<br><br>**Constraints**: *Maximum Length*: `1` |
| `status_description` | [`StatusDescription1Enum`](../../doc/models/status-description-1-enum.md) | Optional | Payment Accelerator status code description.<br><br>**Constraints**: *Maximum Length*: `12` |
| `last_updated_date_time` | `str` | Optional | Status update date in UTC format<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `split_percentage_to_bank_account` | `float` | Optional | Settlement percentage to bank account, remaining goes to Prepay card<br><br>**Constraints**: `>= 0`, `<= 95` |

## Example (as JSON)

```json
{
  "statusCode": "Q",
  "statusDescription": "PENDING",
  "splitPercentageToBankAccount": 21.0,
  "lastUpdatedDateTime": "lastUpdatedDateTime4"
}
```

