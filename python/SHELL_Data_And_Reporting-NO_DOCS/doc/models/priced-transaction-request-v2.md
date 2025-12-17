
# Priced Transaction Request V2

## Structure

`PricedTransactionRequestV2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filters` | [`PricedRequestData`](../../doc/models/priced-request-data.md) | Optional | This endpoint allows querying the transaction data (i.e. Priced, Billed and Unbilled sales items) from SFSBI. It provides a flexible search criteria and supports paging |
| `page` | `int` | Optional | Specify the page of results to be returned. |
| `page_size` | `int` | Optional | Specify the number of records to returned; Max 1000 |

## Example (as JSON)

```json
{
  "Filters": {
    "ColCoCode": "ColCoCode8",
    "InvoiceStatus": "U",
    "PayerNumber": "PayerNumber0",
    "AccountId": 108,
    "AccountNumber": "AccountNumber2",
    "DriverName": "DriverName8",
    "CardGroupId": 154,
    "CardPAN": "CardPAN8"
  },
  "Page": 230,
  "PageSize": 210
}
```

