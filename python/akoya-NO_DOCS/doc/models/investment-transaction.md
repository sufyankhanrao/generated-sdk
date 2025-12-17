
# Investment Transaction

Investment Transactions

*This model accepts additional fields of type Any.*

## Structure

`InvestmentTransaction`

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
| `accrued_interest` | `float` | Optional | Accrued Interest. |
| `commission` | `float` | Optional | Transaction commission. |
| `confirmation_number` | `str` | Optional | Confirmation number of the transaction. |
| `face_value` | `float` | Optional | Cash value for bonds. |
| `fees` | `float` | Optional | Fees applied to the trade. |
| `fractional_cash` | `float` | Optional | Cash for fractional units (used for stock splits). |
| `gain` | `float` | Optional | For sales. |
| `income_type` | [`IncomeType`](../../doc/models/income-type.md) | Optional | Type of investment income. CGLONG (capital gains-long term), CGSHORT (capital gains-short term), MISC. |
| `inv_401_k_source` | [`Inv401KSource`](../../doc/models/inv-401-k-source.md) | Optional | For 401(k) accounts, source of money for this order. Default if not present is OTHERNONVEST. |
| `load` | `float` | Optional | Load on the transaction. |
| `loan_id` | `str` | Optional | For 401k accounts only. This indicates the transaction was due to a loan or a loan repayment. |
| `loan_interest` | `float` | Optional | How much loan pre-payment is interest. |
| `loan_principal` | `float` | Optional | How much loan pre-payment is principal. |
| `markup` | `float` | Optional | Portion of unit price that is attributed to the dealer markup. |
| `new_units` | `float` | Optional | Number of shares after split. |
| `old_units` | `float` | Optional | Number of shares before split. |
| `payroll_date` | `str` | Optional | The date for the 401k transaction was obtained in payroll. |
| `penalty` | `float` | Optional | Indicates amount withheld due to a penalty. |
| `position_type` | [`PositionType`](../../doc/models/position-type.md) | Optional | LONG, SHORT. |
| `price` | `float` | Optional | Unit purchase price. |
| `prior_year_contrib` | `bool` | Optional | Indicates this buy was made using prior years contribution. TRUE or FALSE. |
| `running_balance` | `float` | Optional | Running balance of the position. |
| `security_id` | `str` | Optional | Unique identifier of security. |
| `security_id_type` | [`InvestmentTransactionSecurityIdType`](../../doc/models/investment-transaction-security-id-type.md) | Optional | Security identifier type. |
| `security_type` | [`SecurityType`](../../doc/models/security-type.md) | Optional | - |
| `shares` | `float` | Optional | Number of shares (with decimals). Negative numbers indicate securities are being removed from the account. |
| `split_ratio_denominator` | `float` | Optional | Split ratio denominator. |
| `split_ratio_numerator` | `float` | Optional | Split ratio numerator. |
| `state_withholding` | `float` | Optional | State tax withholding. |
| `sub_account_fund` | [`SubAccountFund`](../../doc/models/sub-account-fund.md) | Optional | From which account money came in. |
| `sub_account_sec` | [`SubAccountSecurityType`](../../doc/models/sub-account-security-type.md) | Optional | Sub-account security type. |
| `symbol` | `str` | Optional | Ticker symbol. |
| `taxes` | `float` | Optional | Taxes on the trade. |
| `tax_exempt` | `bool` | Optional | Tax-exempt transaction TRUE or FALSE. |
| `transaction_reason` | [`TransactionReason`](../../doc/models/transaction-reason.md) | Optional | Reason for this transaction; CALL (the debt was called), SELL (the debt was sold), MATURITY (the debt reached maturity) |
| `transaction_type` | [`InvestmentTransactionType`](../../doc/models/investment-transaction-type.md) | Optional | InvestmentTransaction Type |
| `transfer_action` | [`TransferAction`](../../doc/models/transfer-action.md) | Optional | Transfer direction. |
| `unit_price` | `float` | Optional | Price per commonly-quoted unit. Does not include markup/markdown, unitprice. Share price for stocks, mutual funds, and others. Percentage of par for bonds. Per share (not contract) for options. |
| `units` | `float` | Optional | For security-based actions other than stock splits, quantity. Shares for stocks, mutual funds, and others. Face value for bonds. Contracts for options. |
| `unit_type` | [`UnitType`](../../doc/models/unit-type.md) | Optional | Type of unit. |
| `withholding` | `float` | Optional | Federal tax withholding. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "accountId": "accountId2",
  "amount": 139.34,
  "category": "category0",
  "debitCreditMemo": "DEBIT",
  "description": "description2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

