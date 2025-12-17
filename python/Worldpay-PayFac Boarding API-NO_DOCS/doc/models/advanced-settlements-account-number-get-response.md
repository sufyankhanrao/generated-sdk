
# Advanced Settlements Account Number Get Response

## Structure

`AdvancedSettlementsAccountNumberGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `advanced_settlement_account` | [`AdvancedSettlementAccount`](../../doc/models/advanced-settlement-account.md) | Optional | Provides information about the various advanced settlement options and associated bank accounts |

## Example (as JSON)

```json
{
  "correlationId": "correlationId2",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage2",
  "advancedSettlementAccount": {
    "bankAccount": {
      "ddaType": "Checking",
      "achType": "CommercialChecking",
      "accountNumber": "accountNumber4",
      "routingNumber": "routingNumber0"
    },
    "settlementCategories": [
      "DebitDeposits",
      "DebitChargebacks",
      "DebitConvenienceFees"
    ],
    "oneACHForAllCategories": "Yes",
    "oneACHForCreditAndDebit": "Yes"
  }
}
```

