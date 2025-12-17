
# Card Exceptions

## Structure

`CardExceptions`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_id` | `int` | Optional | Account Id |
| `account_number` | `str` | Optional | Account Number |
| `account_short_name` | `str` | Optional | Account Short Name |
| `card_id` | `int` | Optional | Unique Card Id |
| `currency_code` | `str` | Optional | ISO currency code |
| `currency_symbol` | `str` | Optional | Currency symbol of the Invoice Currency Code |
| `day` | `int` | Optional | Summary Day: Populated when the Period is passed as ‘Day’. |
| `driver_name` | `str` | Optional | Driver name |
| `month` | `int` | Optional | Summary Month: Populated when the Value of Period is Passed as ‘Month’. |
| `pan` | `str` | Optional | Card PAN |
| `payer_id` | `int` | Optional | Payment customer id of the customer |
| `payer_number` | `str` | Optional | Payment customer number |
| `payer_short_name` | `str` | Optional | Payer Short Name |
| `total_amount` | `float` | Optional | Total Amount (In Customer Currency) of Transactions met with the given exceptions criteria. |
| `total_quantity` | `int` | Optional | Total Quantity of Transactions met with the given exceptions criteria. |
| `total_sales_items` | `int` | Optional | Total number of Sales Items met with the given exception criteria. |
| `total_transactions` | `int` | Optional | Total number of Transactions met with the given exception criteria. |
| `vrn` | `str` | Optional | Vehicle Registration Number |
| `week` | `int` | Optional | Summary Week Number with in the given date range. Populated when the Value of Period is Passed as ‘Week’. |
| `year` | `int` | Optional | Summary Year: Populated when the Value of Period is Passed as ‘Month’. |

## Example (as JSON)

```json
{
  "AccountId": 224,
  "AccountNumber": "AccountNumber4",
  "AccountShortName": "AccountShortName6",
  "CardId": 130,
  "CurrencyCode": "CurrencyCode2"
}
```

