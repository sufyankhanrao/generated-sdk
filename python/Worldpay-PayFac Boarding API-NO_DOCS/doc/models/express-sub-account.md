
# Express Sub Account

Express gateway information

## Structure

`ExpressSubAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `express_gateway_id` | `int` | Optional | Express Gateway Id associated with the chain code - used to board to express |
| `batch_close_method` | [`BatchCloseMethodEnum`](../../doc/models/batch-close-method-enum.md) | Optional | The options are Time Initiated or Merchant Initiated. Default Value is TimeInitiated.<br><br>**Default**: `"TimeInitiated"` |
| `batch_close_time` | `str` | Optional | The time in Central Time (CT) that the transactions are settled each day. Required if Batch Close Method is set to Auto (Time Initiated).  Format should be hh:mm:ss (in CT). Default Value is 20:00:00 (in CT)<br><br>**Default**: `"20:00:00"`<br><br>**Constraints**: *Pattern*: `^(0[0-9]\|1[0-9]\|2[0-3]):[0-5][0-9]:[0-5][0-9]$` |
| `check_for_duplicate_transactions` | [`CheckForDuplicateTransactionsEnum`](../../doc/models/check-for-duplicate-transactions-enum.md) | Optional | The same card number submitted for a same general transaction type and amount within the last 25 transactions of the current open batch will be rejected in real-time as a duplicate decline.  Default Value is Yes.<br><br>**Default**: `"Yes"` |
| `account_token` | `str` | Optional | - |
| `account_id` | `str` | Optional | - |
| `acceptor_id` | `str` | Optional | - |
| `default_terminal_id` | `str` | Optional | - |
| `enable_commercial_card_bin_query` | [`EnableCommercialCardBINQueryEnum`](../../doc/models/enable-commercial-card-bin-query-enum.md) | Optional | Feature on Express to allow submerchants to send level 3 data with card transactions |

## Example (as JSON)

```json
{
  "expressGatewayId": 123456,
  "batchCloseMethod": "TimeInitiated",
  "batchCloseTime": "20:00:00",
  "checkForDuplicateTransactions": "Yes",
  "enableCommercialCardBINQuery": "No",
  "accountToken": "accountToken0"
}
```

