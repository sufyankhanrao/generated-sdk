
# Search Auth Non Real Transactions Request

Used to search non-real time authorization transaction.

## Structure

`SearchAuthNonRealTransactionsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination` | [`PaginationType1`](../../doc/models/pagination-type-1.md) | Optional | Used for pagination. |
| `sort_results_by` | [`SortResultsBy`](../../doc/models/sort-results-by.md) | Optional | Sort results by option for non-real time authorization transactions. |
| `hierarchy` | [`Entity`](../../doc/models/entity.md) | Required | Hierarchy details |
| `date_range` | [`SearchAuthTransactionsRequestTransactionDateRange`](../../doc/models/search-auth-transactions-request-transaction-date-range.md) | Required | Refers to number of dates that includes a particular start and end date and all dates in between specific periods of time.<br> Date range supported<br><br>07 Days<br>Independent Sales Organization(SO)<br>Independent Sales Affiliate(SA)<br>National(NL)<br>Partner(PT)<br>Super Chain(SC)<br><br>45 days<br>Chain(CH), Merchant(MT). |
| `transaction_amount_range` | [`SearchAuthTransactionsRequestTransactionAmountRange`](../../doc/models/search-auth-transactions-request-transaction-amount-range.md) | Optional | Transaction amount range. |
| `authorization_code` | `str` | Optional | Authorization codes are used for any transaction that has restrictions on which users are entitled to access. Authorization Code is a six number code from the issuing bank to the vendor, that authorizes the sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_types` | `str` | Optional | Types of card used for the payment. <br> Possible values are CREDIT, DEBIT, GIFT.<br><br>**Constraints**: *Maximum Length*: `6` |
| `card_networks` | [`List[NonrealCardNetworkEnum]`](../../doc/models/nonreal-card-network-enum.md) | Optional | Network the card is associated with facilitating the payment. |
| `token` | `str` | Optional | Tokenization is a substitution for Primary AccountNumber (PAN) with proxy data. Tokenization limits the ability to conduct fraudulent payment transactions. A token value is numeric and is the same length as the card account number length. Max length of token is 19 characters.<br><br>**Constraints**: *Maximum Length*: `19` |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transfer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_type_code` | [`TransactionTypeCodeEnum`](../../doc/models/transaction-type-code-enum.md) | Optional | Indicates the type of transaction that involves funds transfers or a financial transaction. <br> GA - ACTIVATION <BR> GAX- ACTVN REVSL <BR> GB- ADDRESS VERIFY <BR> GC- BAL TRNSFR <BR> GCX- BALANCE INQUIRY <BR> GE- CARD FROM TOKEN <BR> GEX- CASH ADVANCE <BR> GF- CLOSE <BR> GFX- CLOSE REVERSAL <BR> GK- CNVRT HV LVT <BR> GL- INACTIVITY FEES <BR> GLX- MAIL ORDER<BR> GM- MAIL/PHO ADVICE<BR> GP- MAKE KEY ADVCON<BR> GPX- MAKE KEY ADVICE<BR> GS- MAKE KEY ADVSTG<BR> GU- MAKE KEY REQUES<BR> GUX- MINISTMT<BR> GV- PARTIAL REVRSL<BR> GVX- PREAUT COMP REV<BR> GZ- PREAUTH COMPLTN<BR> GZX- PREAUTH REQUEST<BR> G1- PREAUTH RQ REV<BR> IC- PREPAID ACT REV<BR> IF- PREPAID ACTVN<BR> IL- PREPAID LD REV<BR> IM- PREPAID LOAD<BR> IP- PURCHASE<BR> IR- PARTIAL REVRSL<BR> IS- PURCHASE ADVICE<BR> IV- PURCHASE REVRSL<BR> IX- REFUND<BR> KA- REFUND REVERSAL<BR> KC- RELOAD<BR> KM- RELOAD REVERSAL<BR> KS- REVERSAL<BR> MM- REVERSAL<BR> MP- STATUS/UNSTATUS<BR> RF- TOKEN FROM CARD<BR> RL- UNLOAD<BR> TC- UNLOAD REVERSAL<BR> TK- VIRTL ACTVN<BR> TR- VIRTL ACTVN REV<BR> 00- INCOMPLETE TRAN<BR> 01- DB WITH<BR> 02- DB WITH<BR> 06- SPECIAL TRAN<BR> 10- POS DB CRD PUR<BR> 11- POS DB CRD RET<BR> 12- POS DB INQ<BR> 13- POS PRE AUTH DB<BR> 14- POS PRE ATH<BR> 15- POS DB INQ<BR> 16- POS PRE AUTH DB<BR> 17- POS PRE ATH<BR> 25- CHECK VERIFY<BR> 29- POS CR CRD PUR<BR> 30- POS CR CRD RET<BR> 31- POS CR CRD PUR <BR> 32- POS CR CRD RET <BR> 38- CC AUTH <BR> 39- CC COMPLETION <BR> 40- CC AUTH <BR> 41- CC COMPLETION <BR> 48- INTERBANK DR <BR> 49- INTERBANK CR <BR><br><br>**Constraints**: *Maximum Length*: `3` |
| `transaction_status_code` | [`TransactionStatusCodeEnum`](../../doc/models/transaction-status-code-enum.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made.<br> AA - APPROVAL<br> AB - APPRVL FOR LESS<br> AV - APPROVAL, VIP<br> EX -  DUPLICATE TRANS<br> F1 -  FRAUD,PCKUP CRD<br> NC -  DECLINE, PICKUP<br> ND -  DECLINE<br> NE -  DECLINE,EXPIRED<br> NL -  CRD LIMT EXCEED<br> NP -  INVALID/BAD PIN<br> NR -  REFER,CALL BANK<br> NS -  DECLINE,SPECIAL<br> NX -  ACK REFUND RQST<br> N7 -  CVV2 INVALID<br> RE -  RETRY<br> RJ -  EDIT REJECT<br> V1 -  EXCEEDS COUNT<br> V2 -  EXCEEDS AMOUNT<br> V3 -  EXCEEDS CNT/AMT<br> V4 -  VLCTY NEGATIVE<br> V5 -  VLCTY FRAUD<br> V6 -  NO ZIP MATCH<br> 000 -  TRANSACTION AUT<br> 001 -  INVALID CARD OR<br> 002 -  INVALID CARD NU<br> 003 -  CARD HAS EXPIRE<br> 004 -  CC  REC,NO XREF<br> 005 -  CLUSTER NOT ACC<br> 006 -  CC  CARD STATUS<br> 007 - CC  ACCT CLOSED<br> 008 -  PIN MISSING<br> 009 -  JIMMY(RETAIN)<br> 010 -  INVALID SPECIAL<br> 011 -  SPECIAL TRANS P<br> 012 -  SIGNON BEFORE S<br> 013 -  SIGNON SEQUENCE<br> 014 -  NO FROM ACCT<br> 015 -  FROM ACCT HAS N<br> 016 -  FROM ACCT NOT A<br> 017 -  FROM ACCT HAS N<br> 018 -  INSUFFICIENT BA<br> 019 -  INSUFFICIENT BA<br> 020 -  RR ACCT NOT ACC<br> 021 -  NO TO ACCT<br> 022 -  TO ACCT HAS NO<br> 023 -  INVALID ATM COD<br> 024 -  DAILY CLUSTER L<br> 025 -   TO ACCT NOT ACC<br> 026 -  CC  RECORD DOES<br> 027 -  DEPOSITORY FULL<br> 028 -  DAILY ACCT LIMI<br> 029 -  ATM OUT OF CASH<br> 030 -  CLUSTER STATUS<br> 031 -  ACCT STATUS ABN<br> 032 -  RR STATUS ABNOR<br> 033 -  TO ACCT STATUS<br> 034 -  091,092 CANNOT<br> 035 -  093,094 CANNOT<br> 036 -  TERMINAL OUT OF<br> 037 -  FROM ACCT CLOSE<br> 038 -  TO ACCT CLOSED<br> 039 -  RR ACCT CLOSED<br> 040 -  NO RR CONNECTED<br> 041 -  RR AND TO ACCT<br> 042 -  CUSTOMER CANCEL<br> 043 -  CLERK CANCEL<br> 044 -  INVALID PIN-TOO<br> 045 -  SIGNON,ADD AMOU<br> 046 -  SIGNON NOT INIT<br> 047 -  INTERNAL PROB(M<br> 048 -  LOGON INBETWEEN<br> 049 -  CLUSTER CLOSED(<br><br><br>**Constraints**: *Maximum Length*: `3` |
| `reference_number` | `str` | Optional | Refers to a key to uniquely identify a card transaction based on the ISO 8583 standard.<br><br>**Constraints**: *Maximum Length*: `16` |
| `fraud_fields` | [`Fraudfields`](../../doc/models/fraudfields.md) | Optional | Fraud fields are data points in a transaction record. |

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
  "dateRange": {
    "fromDate": "2021-12-01",
    "toDate": "2022-01-01"
  },
  "authorizationCode": "73994M",
  "token": "374245111181117",
  "transactionTypeCode": "GA",
  "transactionStatusCode": "AA",
  "referenceNumber": "2444600338440029",
  "pagination": {
    "pageNumber": 16776215,
    "pageSize": 1000
  },
  "sortResultsBy": {
    "fieldName": "BATCH_NUMBER",
    "orderBy": "ASC"
  },
  "transactionAmountRange": {
    "fromAmount": 130.84,
    "toAmount": 8.76,
    "authorizationCurrencyCode": "authorizationCurrencyCode6"
  },
  "cardTypes": "cardTypes4"
}
```

