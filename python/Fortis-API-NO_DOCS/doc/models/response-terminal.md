
# Response Terminal

## Structure

`ResponseTerminal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type74Enum`](../../doc/models/type-74-enum.md) | Optional | Resource Type<br><br>**Default**: `'Terminal'` |
| `data` | [`Data19`](../../doc/models/data-19.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "Terminal",
  "data": {
    "location_id": "location_id4",
    "default_product_transaction_id": "default_product_transaction_id6",
    "terminal_application_id": "terminal_application_id0",
    "terminal_cvm_id": "terminal_cvm_id0",
    "terminal_manufacturer_code": "1"
  }
}
```

