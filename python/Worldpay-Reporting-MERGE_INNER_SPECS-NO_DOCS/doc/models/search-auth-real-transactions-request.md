
# Search Auth Real Transactions Request

Used to search real time authorization transaction.

## Structure

`SearchAuthRealTransactionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination |
| `sort_results_by` | [`SortResultsBy`](../../doc/models/sort-results-by.md) | Optional | Sort results by option for real time authorization transactions. |
| `hierarchy` | [`Entity`](../../doc/models/entity.md) | Required | Hierarchy details. |
| `transaction_date_range` | [`SearchAuthTransactionsRequestRealTimeTransactionDateRange`](../../doc/models/search-auth-transactions-request-real-time-transaction-date-range.md) | Required | Transaction date range. |
| `transaction_time_range` | [`SearchAuthTransactionsRequestTransactionTimeRange`](../../doc/models/search-auth-transactions-request-transaction-time-range.md) | Optional | Transaction time range. |
| `transaction_amount_range` | [`SearchAuthTransactionsRequestTransactionAmountRange`](../../doc/models/search-auth-transactions-request-transaction-amount-range.md) | Optional | Transaction amount range. |
| `authorization_code` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_type` | [`CardTypeEnum`](../../doc/models/card-type-enum.md) | Optional | Types of card used for the payment. <br> Possible values are CREDIT, DEBIT, GIFT.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_networks` | [`List[CardNetworkEnum]`](../../doc/models/card-network-enum.md) | Optional | Network the card is associated with facilitating the payment.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `19` |
| `card_number` | `str` | Optional | This is the number found on the card used to make a purchase, also referred to as the bank card number.<br>Searches can be done on the full card number, on the first 6 and last 4 digits, or on the last 4 digit searches.<br><br>**Constraints**: *Maximum Length*: `19` |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transfer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_type` | [`TransactionTypeEnum`](../../doc/models/transaction-type-enum.md) | Optional | Indicates the type of transaction that involves funds transfers or a financial transaction. |
| `transaction_status` | [`TransactionStatusEnum`](../../doc/models/transaction-status-enum.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made. <br> AA - APPROVAL<br> AB - APPRVL FOR LESS<br> AV - APPROVAL, VIP<br> EX -  DUPLICATE TRANS<br> F1 -  FRAUD,PCKUP CRD<br> NC -  DECLINE, PICKUP<br> ND -  DECLINE<br> NE -  DECLINE,EXPIRED<br> NL -  CRD LIMT EXCEED<br> NP -  INVALID/BAD PIN<br> NR -  REFER,CALL BANK<br> NS -  DECLINE,SPECIAL<br> NX -  ACK REFUND RQST<br> N7 -  CVV2 INVALID<br> RE -  RETRY<br> RJ -  EDIT REJECT<br> V1 -  EXCEEDS COUNT<br> V2 -  EXCEEDS AMOUNT<br> V3 -  EXCEEDS CNT/AMT<br> V4 -  VLCTY NEGATIVE<br> V5 -  VLCTY FRAUD<br> V6 -  NO ZIP MATCH<br> 000 -  TRANSACTION AUT<br> 001 -  INVALID CARD OR<br> 002 -  INVALID CARD NU<br> 003 -  CARD HAS EXPIRE<br> 004 -  CC  REC,NO XREF<br> 005 -  CLUSTER NOT ACC<br> 006 -  CC  CARD STATUS<br> 007 - CC  ACCT CLOSED<br> 008 -  PIN MISSING<br> 009 -  JIMMY(RETAIN)<br> 010 -  INVALID SPECIAL<br> 011 -  SPECIAL TRANS P<br> 012 -  SIGNON BEFORE S<br> 013 -  SIGNON SEQUENCE<br> 014 -  NO FROM ACCT<br> 015 -  FROM ACCT HAS N<br> 016 -  FROM ACCT NOT A<br> 017 -  FROM ACCT HAS N<br> 018 -  INSUFFICIENT BA<br> 019 -  INSUFFICIENT BA<br> 020 -  RR ACCT NOT ACC<br> 021 -  NO TO ACCT<br> 022 -  TO ACCT HAS NO<br> 023 -  INVALID ATM COD<br> 024 -  DAILY CLUSTER L<br> 025 -   TO ACCT NOT ACC<br> 026 -  CC  RECORD DOES<br> 027 -  DEPOSITORY FULL<br> 028 -  DAILY ACCT LIMI<br> 029 -  ATM OUT OF CASH<br> 030 -  CLUSTER STATUS<br> 031 -  ACCT STATUS ABN<br> 032 -  RR STATUS ABNOR<br> 033 -  TO ACCT STATUS<br> 034 -  091,092 CANNOT<br> 035 -  093,094 CANNOT<br> 036 -  TERMINAL OUT OF<br> 037 -  FROM ACCT CLOSE<br> 038 -  TO ACCT CLOSED<br> 039 -  RR ACCT CLOSED<br> 040 -  NO RR CONNECTED<br> 041 -  RR AND TO ACCT<br> 042 -  CUSTOMER CANCEL<br> 043 -  CLERK CANCEL<br> 044 -  INVALID PIN-TOO<br> 045 -  SIGNON,ADD AMOU<br> 046 -  SIGNON NOT INIT<br> 047 -  INTERNAL PROB(M<br> 048 -  LOGON INBETWEEN<br> 049 -  CLUSTER CLOSED(<br> |
| `customer_fields` | [`CustomerFields`](../../doc/models/customer-fields.md) | Optional | Customer details. |
| `fraud_score` | [`SearchAuthRealTransactionsRequestFraudScore`](../../doc/models/search-auth-real-transactions-request-fraud-score.md) | Optional | Fraud score is a measure that helps gauge risk involved with orders before processing. |
| `fraud_response_code` | [`FraudResponseCodeEnum`](../../doc/models/fraud-response-code-enum.md) | Optional | Predefined set of codes that determines various types of fraudulent activities to classify accordingly.<br><br>**Constraints**: *Maximum Length*: `256` |
| `fraud_rule_result` | [`FraudRuleResultEnum`](../../doc/models/fraud-rule-result-enum.md) | Optional | The result of the decision made from the Fraud rule applied for the transaction.<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "hierarchy": {
    "level": "INDEPENDENT_SALES_ORGANIZATION",
    "values": [
      "4445000860700",
      "4445000860702"
    ],
    "chainCode": "OA1234"
  },
  "transactionDateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2021-12-01"
  },
  "authorizationCode": "73994M",
  "cardType": "CREDIT",
  "cardNumber": "************4353",
  "token": "374245111181117",
  "transactionType": "GA",
  "transactionStatus": "AA",
  "fraudResponseCode": "FRAUD_SYSTEM_APPROVED",
  "fraudRuleResult": "MANUAL_REVIEW",
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  },
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  },
  "transactionTimeRange": {
    "fromTime": "fromTime8",
    "toTime": "toTime4"
  },
  "transactionAmountRange": {
    "fromAmount": 130.84,
    "toAmount": 8.76,
    "authorizationCurrencyCode": "authorizationCurrencyCode6"
  }
}
```

