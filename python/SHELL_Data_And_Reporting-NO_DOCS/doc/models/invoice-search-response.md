
# Invoice Search Response

## Structure

`InvoiceSearchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | API Request Id |
| `status` | `str` | Optional | Indicates overall status of the request. Allowed values: SUCCES, FAILED |
| `data` | [`List[InvoiceSearchDetails]`](../../doc/models/invoice-search-details.md) | Optional | - |
| `page` | `int` | Optional | Specifies the returned page of the results |
| `page_size` | `int` | Optional | Specifies the number of records to be returned which could be less than the PageSize in the request |
| `total_records` | `int` | Optional | Specifies the total records available in the result |
| `total_pages` | `int` | Optional | Specifies the total pages available in the result |

## Example (as JSON)

```json
{
  "RequestId": "RequestId0",
  "Status": "Status6",
  "Data": [
    {
      "AccountFullName": "AccountFullName6",
      "AccountId": 62,
      "AccountNumber": "AccountNumber8",
      "AccountShortName": "AccountShortName0",
      "ColCoId": 210
    },
    {
      "AccountFullName": "AccountFullName6",
      "AccountId": 62,
      "AccountNumber": "AccountNumber8",
      "AccountShortName": "AccountShortName0",
      "ColCoId": 210
    },
    {
      "AccountFullName": "AccountFullName6",
      "AccountId": 62,
      "AccountNumber": "AccountNumber8",
      "AccountShortName": "AccountShortName0",
      "ColCoId": 210
    }
  ],
  "Page": 226,
  "PageSize": 206
}
```

