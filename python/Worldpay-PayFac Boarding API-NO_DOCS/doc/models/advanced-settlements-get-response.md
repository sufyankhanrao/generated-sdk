
# Advanced Settlements Get Response

## Structure

`AdvancedSettlementsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `advanced_settlement_accounts` | [`List[AdvancedSettlementAccount]`](../../doc/models/advanced-settlement-account.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "advancedSettlementAccounts": [
    {
      "bankAccount": {
        "ddaType": "Checking",
        "achType": "CommercialChecking",
        "accountNumber": "accountNumber4",
        "routingNumber": "routingNumber0"
      },
      "settlementCategories": [
        "CreditConvenienceFees"
      ],
      "oneACHForAllCategories": "Yes",
      "oneACHForCreditAndDebit": "Yes"
    },
    {
      "bankAccount": {
        "ddaType": "Checking",
        "achType": "CommercialChecking",
        "accountNumber": "accountNumber4",
        "routingNumber": "routingNumber0"
      },
      "settlementCategories": [
        "CreditConvenienceFees"
      ],
      "oneACHForAllCategories": "Yes",
      "oneACHForCreditAndDebit": "Yes"
    }
  ]
}
```

