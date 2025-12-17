
# Response Recurring

## Structure

`ResponseRecurring`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type59Enum`](../../doc/models/type-59-enum.md) | Optional | Resource Type<br><br>**Default**: `'Recurring'` |
| `data` | [`Data16`](../../doc/models/data-16.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "Recurring",
  "data": {
    "account_vault_id": "account_vault_id6",
    "token_id": "token_id4",
    "contact_id": "contact_id4",
    "account_vault_api_id": "account_vault_api_id4",
    "token_api_id": "token_api_id6"
  }
}
```

