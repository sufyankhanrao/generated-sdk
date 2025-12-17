
# Tax Refund Direct Deposit

IRS Form 8888 Direct Deposit Information

*This model accepts additional fields of type Any.*

## Structure

`TaxRefundDirectDeposit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `institution_name` | `str` | Optional | Name of institution |
| `rtn` | `str` | Optional | Routing transit number |
| `account_number` | `str` | Optional | Account number |
| `account_nick_name` | `str` | Optional | Account nickname |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "institutionName": "institutionName6",
  "rtn": "rtn0",
  "accountNumber": "accountNumber4",
  "accountNickName": "accountNickName4",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

