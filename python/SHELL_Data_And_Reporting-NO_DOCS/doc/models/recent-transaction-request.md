
# Recent Transaction Request

## Structure

`RecentTransactionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page_size` | `int` | Required | Specify the number of records to returned; Max 1000<br><br>**Constraints**: `>= 1`, `<= 1000` |
| `page` | `int` | Required | Specify the page of results to be returned.<br><br>**Constraints**: `<= 1` |
| `filters` | [`RecentTransactionReq`](../../doc/models/recent-transaction-req.md) | Required | - |

## Example (as JSON)

```json
{
  "PageSize": 1,
  "Page": 1,
  "Filters": {
    "ColCoCode": 14,
    "PayerNumber": "GB00001232",
    "AccountNumber": "GB00001233",
    "ProductCode": "22",
    "PurchasedInCountry": "GB",
    "CardPAN": "700205******890645",
    "FromDateTime": "2020-11-09 13:56:03.000",
    "ToDateTime": "2020-12-09 13:56:03.000",
    "TransactionStatus": "APPROVED",
    "FuelOnly": "False",
    "ProductGroupName": "Motor gasoline",
    "VehicleRegistrationNumber": "YG67OUM",
    "IncludeDeclines": true,
    "CardIssuerName": "Mathew",
    "ColumnList": "PayerNumber,AccountNumber,ProductName,FuelVolume,PAN"
  }
}
```

