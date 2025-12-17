
# Default Bank Accounts Get Response

## Structure

`DefaultBankAccountsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `bank_account` | [`BankAccount`](../../doc/models/bank-account.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "bankAccount": {
    "ddaType": "Checking",
    "achType": "CommercialChecking",
    "accountNumber": "accountNumber4",
    "routingNumber": "routingNumber0"
  }
}
```

