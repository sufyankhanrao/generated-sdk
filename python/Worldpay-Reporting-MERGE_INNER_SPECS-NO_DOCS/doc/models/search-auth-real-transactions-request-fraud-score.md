
# Search Auth Real Transactions Request Fraud Score

Fraud score is a measure that helps gauge risk involved with orders before processing.

## Structure

`SearchAuthRealTransactionsRequestFraudScore`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `from_score` | `float` | Optional | Starting fraud score<br><br>**Constraints**: `>= 0`, `<= 100` |
| `to_score` | `float` | Optional | Ending fraud score<br><br>**Constraints**: `>= 0`, `<= 100` |

## Example (as JSON)

```json
{
  "fromScore": 0.13,
  "toScore": 0.84
}
```

