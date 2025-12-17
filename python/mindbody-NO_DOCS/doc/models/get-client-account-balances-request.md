
# Get Client Account Balances Request

## Structure

`GetClientAccountBalancesRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_date` | `datetime` | Optional | The date you want a balance relative to.<br>Default: **the current date** |
| `class_id` | `int` | Optional | The class ID of the event for which you want a balance. |
| `client_ids` | `List[str]` | Required | The list of clients IDs for which you want account balances. |
| `limit` | `int` | Optional | Number of results to include, defaults to 100 |
| `offset` | `int` | Optional | Page offset, defaults to 0. |

## Example (as JSON)

```json
{
  "BalanceDate": "2016-03-13T12:52:32.123Z",
  "ClassId": 156,
  "ClientIds": [
    "ClientIds9"
  ],
  "Limit": 98,
  "Offset": 32
}
```

