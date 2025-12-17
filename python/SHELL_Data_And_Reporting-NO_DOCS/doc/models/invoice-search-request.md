
# Invoice Search Request

## Structure

`InvoiceSearchRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `filters` | [`InvoiceSearchRequestFilters`](../../doc/models/invoice-search-request-filters.md) | Optional | - |
| `page_size` | `int` | Optional | - |
| `page` | `int` | Optional | - |
| `sort_by` | `List[int]` | Optional | Sort option –<br><br>1. InvoiceDate ASC<br>2. InvoiceDate DESC<br>3. NetAmountCustomerCurrency ASC<br>4. NetAmountCustomerCurrency DESC<br>   Optional<br>   Note:<br>   This option uses a column name with a combination of “ASC or DESC” for sorting.<br>   If only the column name is provided, it is sorted by ascending.<br>   Example values to be passed:<br>   [“InvoiceDate”, “NetAmountCustomerCurrency DESC”] |

## Example (as JSON)

```json
{
  "Filters": {
    "ColCoId": 0,
    "PayerId": 48,
    "PayerNumber": "PayerNumber0",
    "InvoiceId": 188,
    "InvoiceNumber": "InvoiceNumber0"
  },
  "PageSize": 244,
  "Page": 8,
  "SortBy": [
    83,
    84
  ]
}
```

