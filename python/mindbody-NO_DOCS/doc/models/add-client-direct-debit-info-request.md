
# Add Client Direct Debit Info Request

## Structure

`AddClientDirectDebitInfoRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test` | `bool` | Optional | When `true`, indicates that test mode is enabled. The information is to be validated, but no data will be added or updated.<br>Default: **false** |
| `client_id` | `str` | Optional | The ID of the client being updated |
| `name_on_account` | `str` | Optional | The name on the bank account being added |
| `routing_number` | `str` | Optional | The routing number of the bank account being added |
| `account_number` | `str` | Optional | The bank account number |
| `account_type` | `str` | Optional | The account type.<br><br>Possible values:<br><br>* Checking<br>* Savings |

## Example (as JSON)

```json
{
  "Test": false,
  "ClientId": "ClientId8",
  "NameOnAccount": "NameOnAccount8",
  "RoutingNumber": "RoutingNumber4",
  "AccountNumber": "AccountNumber8"
}
```

