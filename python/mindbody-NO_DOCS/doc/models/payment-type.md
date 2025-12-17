
# Payment Type

## Structure

`PaymentType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | The Payment Type Id used for api calls. |
| `payment_type_name` | `str` | Optional | Payment Type Name |
| `active` | `bool` | Optional | Check if Payment type is active. |
| `fee` | `float` | Optional | Payment type fee. |

## Example (as JSON)

```json
{
  "Id": 170,
  "PaymentTypeName": "PaymentTypeName0",
  "Active": false,
  "Fee": 17.74
}
```

