
# Payer Access

## Structure

`PayerAccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `is_default` | `bool` | Optional | Whether this payer is the default payer of the user.<br><br>**Default**: `False` |
| `colco_id` | `int` | Optional | Collecting company id. |
| `colco_code` | `int` | Optional | Collecting company code.<br>Example:<br>86-Philippines<br>5-UK |
| `col_co_country_code` | `str` | Optional | The 2-character ISO Code for the customer and card owning country |
| `payer_group_id` | `int` | Optional | Payer Group Id of the payer. |
| `payer_group` | `str` | Optional | Payer group of the payer.<br>The value of this parameter will always be null when the input parameter “IncludePayerGroup” is false. |
| `payer_id` | `int` | Optional | Payer Id to which the user has access<br>Example: 123456 |
| `payer_number` | `str` | Optional | Payer Number to which the user has access<br>Example: GB000000123 |
| `payer_name` | `str` | Optional | Name of the Payer to which the user has access |

## Example (as JSON)

```json
{
  "IsDefault": false,
  "ColcoId": 14,
  "ColcoCode": 14,
  "ColCoCountryCode": "DE",
  "PayerGroupId": 123,
  "PayerGroup": "null",
  "PayerId": 854,
  "PayerNumber": "DE26688504",
  "PayerName": "TK MobilPlus"
}
```

