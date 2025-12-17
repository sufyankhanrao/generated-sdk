
# Add Client Direct Debit Info Response

## Structure

`AddClientDirectDebitInfoResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | The ID of the client being updated |
| `name_on_account` | `str` | Optional | The name on the bank account being added |
| `routing_number` | `str` | Optional | The routing number of the bank account being added |
| `account_number` | `str` | Optional | The bank account number |
| `account_type` | `str` | Optional | The account type.<br><br>Possible values:<br><br>* Checking<br>* Savings |

## Example (as JSON)

```json
{
  "ClientId": "ClientId8",
  "NameOnAccount": "NameOnAccount8",
  "RoutingNumber": "RoutingNumber2",
  "AccountNumber": "AccountNumber2",
  "AccountType": "AccountType8"
}
```

