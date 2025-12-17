
# Txns Put Request

## Structure

`TxnsPutRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `batch` | `str` | Optional | If the Transaction is linked to a Batch, this field specifies the identifier of the Batch. |
| `debt_repayment` | [`DebtRepaymentEnum`](../../doc/models/debt-repayment-enum.md) | Optional | If this transaction is for debt repayment or not for debt repayment.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Transaction not for debt repayment.**<br>- `1` - **Transaction for debt repayment.**<br><br></details><br>**Default**: `0`<br> |
| `processed_sequence` | `int` | Optional | For entry creation and deletion job sequencing: the current processed sequence number for this transaction. |
| `funded` | `int` | Optional | A date indicating when this Transaction was funded.<br>This field is set automatically. |
| `returned` | `str` | Optional | The transaction has been returned by the receiver. |
| `funding_enabled` | [`TxnsFundingEnabledEnum`](../../doc/models/txns-funding-enabled-enum.md) | Optional | Whether or not funding is enabled for this Transaction.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Disabled.**<br>- `1` - **Enabled.**<br><br></details><br> |
| `request_sequence` | `int` | Optional | For entry creation and deletion job sequencing: the current processed sequence number for this transaction. |
| `token` | `str` | Optional | The token of the Tokens resource this Transaction is associated with. |
| `auth_token_customer` | `str` | Optional | The customer identifier from the AuthToken used during authentication. |
| `channel` | `str` | Optional | This field is stored as a text string and must be between 0 and 1000 characters long. |
| `client_ip` | `str` | Optional | The client ip address from which the Transaction was created.<br>Valid values are any Ipv4 or Ipv6 address. |
| `currency` | [`CurrencyEnum`](../../doc/models/currency-enum.md) | Optional | The currency for this transaction. See <a href="https://www.iban.com/currency-codes" target="_blank">Currency codes</a>  for all valid values. |
| `fee_consumed` | `int` | Optional | When fee is set, this will track the amount of the fee that has been consumed.<br>This field is specified as an integer in cents. |
| `signature` | [`SignatureEnum`](../../doc/models/signature-enum.md) | Optional | Whether a signature was captured during this Transaction. You can set this field if you took a signature for the Transaction. The API also sets this field automatically if you associate a signature to the Transaction by creating a 'txnDatas' resource.<br><br><details><br><summary>Valid Values</summary><br>- `0` - **Not captured.**<br>- `1` - **Captured.**<br><br></details><br> |
| `tmx_session_id` | `str` | Optional | Threatmetrix session ID, used to trace the financial session and prevent possible frauds. |
| `first_txn` | `str` | Optional | For external recurring systems, this is the first transaction ID related to this recurring payment. |

## Example (as JSON)

```json
{
  "currency": "USD",
  "batch": "t1_bth_67b6129bcca1cbb7cdac000",
  "debtRepayment": 1,
  "processedSequence": 0,
  "funded": 623,
  "returned": "Returned Transaction",
  "fundingEnabled": 1,
  "requestSequence": 1,
  "token": "7f36eeabbdce941fb564243936402a00",
  "authTokenCustomer": "Customer Identifier",
  "channel": "LA",
  "clientIp": "216.80.4.000",
  "signature": 1,
  "tmxSessionId": "Threatmetrix session ID",
  "firstTxn": "t1_txn_67b6129bcca1cbb7cdac001"
}
```

