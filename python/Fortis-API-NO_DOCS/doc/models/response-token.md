
# Response Token

## Structure

`ResponseToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type84Enum`](../../doc/models/type-84-enum.md) | Optional | Resource Type<br><br>**Default**: `"Token"` |
| `data` | [`Data21`](../../doc/models/data-21.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "Token",
  "data": {
    "account_holder_name": "account_holder_name0",
    "account_vault_api_id": "account_vault_api_id4",
    "token_api_id": "token_api_id6",
    "accountvault_c1": "accountvault_c14",
    "accountvault_c2": "accountvault_c28"
  }
}
```

