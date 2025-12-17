
# Response Apple Pay Validate Merchant

## Structure

`ResponseApplePayValidateMerchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`Type118Enum`](../../doc/models/type-118-enum.md) | Optional | Resource Type<br><br>**Default**: `"ApplePayValidateMerchant"` |
| `data` | [`Data33`](../../doc/models/data-33.md) | Optional | - |

## Example (as JSON)

```json
{
  "type": "ApplePayValidateMerchant",
  "data": {
    "merchantSession": "merchantSession0"
  }
}
```

