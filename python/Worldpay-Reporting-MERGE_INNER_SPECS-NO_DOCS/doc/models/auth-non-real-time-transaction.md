
# Auth Non Real Time Transaction

Real time authorization transaction.

## Structure

`AuthNonRealTimeTransaction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `str` | Optional | Transaction id is a number generated from the electronic transafer of funds. It is a unique identifier that is generated with every card transaction. (a 12-18 digit code)<br><br>**Constraints**: *Minimum Length*: `12`, *Maximum Length*: `18` |
| `transaction_date_time` | `str` | Optional | Refers to the transaction date and time on which the bank clears the transaction for deposists or withdraws.<br><br>**Constraints**: *Minimum Length*: `19`, *Maximum Length*: `19`, *Pattern*: `^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2})*$` |
| `process_date` | `str` | Optional | Indicates the process date of a transaction that has been authorized between the two parties.<br><br>**Constraints**: *Minimum Length*: `10`, *Maximum Length*: `10`, *Pattern*: `^[0-9]{4}-[0-9]{2}-[0-9]{2}$` |
| `transaction_status` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | This field refers to the transaction status code received at the time a purchase is being made, including the status' short and long descriptions. |
| `transaction_type` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Indicates the type of transaction that occurred when funds are transfered between a merchant and a bank, including its short and long descriptions. |
| `authorization_code` | `str` | Optional | The Authorization Code is a six digit number from the issuing bank to the vendor, authorizing a sale.<br><br>**Constraints**: *Maximum Length*: `6` |
| `authorization_amount` | `float` | Optional | The authorization amount is the transaction amount a merchant submitted to the customer's issuing bank for approval.<br><br>**Constraints**: `>= 0`, `<= 9999999999999.99` |
| `authorization_currency` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Authorization Currency Code defines alpha codes and numeric codes for the representation of currencies and provides information about the relationships between individual currencies and their minor units. Code is as per ISO Standard country code for United States". |
| `reference_number` | `str` | Optional | Refers to a key to uniquely identify a card transaction based on the ISO 8583 standard.<br><br>**Constraints**: *Maximum Length*: `16` |

## Example (as JSON)

```json
{
  "transactionDateTime": "07/19/2016 16:41:31",
  "processDate": "2016-07-19",
  "transactionStatus": {
    "code": "NC",
    "shortDescription": "DECLINE, PICKUP",
    "longDescription": "DECLINE, PICK UP CARD"
  },
  "transactionType": {
    "code": "11",
    "shortDescription": "POS DB CRD RET",
    "longDescription": "POS DEBIT CARD RETURN"
  },
  "authorizationCode": "73994M",
  "authorizationAmount": 3445.56,
  "authorizationCurrency": {
    "code": "840",
    "shortDescription": "USA",
    "longDescription": "USA"
  },
  "referenceNumber": "2444600338440029",
  "transactionId": "transactionId8"
}
```

