
# Loan Transaction

Loan Transaction

*This model accepts additional fields of type Any.*

## Structure

`LoanTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `str` | Optional | Corresponds to AccountId in Account |
| `amount` | `float` | Optional | The amount of money in the account currency.<br><br>If balanceType is `ASSET`:<br><br>1. If `debitCreditMemo` = `DEBIT`, sign is "+" or not present<br>2. If `CREDIT`, sign is "-"<br><br>If balanceType is `LIABILITY`:<br><br>1. If `debitCreditMemo` = `DEBIT`, sign is "-"<br>2. If `CREDIT`, sign is "+" or not present |
| `category` | `str` | Optional | Transaction category, preferably MCC or SIC. |
| `debit_credit_memo` | [`DebitCreditMemo`](../../doc/models/debit-credit-memo.md) | Optional | Akoya will ensure that this is correctly populated with one of DEBIT or CREDIT and matches the sign of the status field. |
| `description` | `str` | Optional | The description of the transaction |
| `image_ids` | `List[str]` | Optional | Array of image identifiers (unique to transaction) used to retrieve images of check or transaction receipt. |
| `fi_attributes` | [`List[FiAttributeEntity]`](../../doc/models/fi-attribute-entity.md) | Optional | Array of FI-specific attributes<br><br>**Constraints**: *Minimum Items*: `1`, *Unique Items Required* |
| `foreign_amount` | `float` | Optional | The amount of money in the foreign currency |
| `foreign_currency` | `str` | Optional | The ISO 4217 code of the foreign currency |
| `line_item` | [`List[LineItem]`](../../doc/models/line-item.md) | Optional | Breakdown of the transaction details |
| `links` | [`List[HateoasLink]`](../../doc/models/hateoas-link.md) | Optional | Links (unique to this Transaction) used to retrieve images of checks or transaction receipts, or invoke other APIs |
| `memo` | `str` | Optional | Secondary transaction description |
| `posted_timestamp` | `datetime` | Optional | The date and time that the transaction was posted to the account. If not provided then TransactionTimestamp can be used as PostedTimeStamp. |
| `reference` | `str` | Optional | A tracking reference identifier |
| `reference_transaction_id` | `str` | Optional | Akoya ensures that this field is populated for all transactions which are reversals, otherwise it is null. Either way it is always present.<br><br>For reverse postings, the identity of the transaction being reversed. For the correction transaction, the identity of the reversing post. For credit card posting transactions, the identity of the authorization transaction. |
| `status` | [`TransationStatus`](../../doc/models/transation-status.md) | Optional | AUTHORIZATION, MEMO, PENDING, or POSTED |
| `sub_category` | `str` | Optional | Transaction category detail |
| `transaction_id` | `str` | Optional | Long term persistent identity of the transaction (unique to account).<br>Transaction IDs should:<br><br>1. be the same for pending and posted<br>2. be different for reversed transactions<br>3. `referenceTransactionId` should be present for reversed transactions' |
| `transaction_timestamp` | `datetime` | Optional | The date and time that the transaction was added to the server backend systems.<br><br>Akoya ensures that this field is populated for all transactions to which it applies, otherwise it is null. Either way it is always present. |
| `payment_details` | [`PaymentDetails`](../../doc/models/payment-details.md) | Optional | Payment details for some transactions |
| `transaction_type` | [`LoanTransactionType`](../../doc/models/loan-transaction-type.md) | Optional | LoanTransaction Type |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId8",
  "amount": 49.0,
  "category": "category6",
  "debitCreditMemo": "DEBIT",
  "description": "description8",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

