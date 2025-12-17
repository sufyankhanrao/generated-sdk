
# Get Packages Response

## Structure

`GetPackagesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `packages` | [`List[Package]`](../../doc/models/package.md) | Optional | Contains information about the resulting packages. |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |

## Example (as JSON)

```json
{
  "Packages": [
    {
      "Id": 68,
      "Name": "Name4",
      "DiscountPercentage": 252.08,
      "SellOnline": false,
      "Services": [
        {
          "Price": 224.3,
          "OnlinePrice": 2.82,
          "TaxIncluded": 75.84,
          "ProgramId": 204,
          "TaxRate": 192.34
        },
        {
          "Price": 224.3,
          "OnlinePrice": 2.82,
          "TaxIncluded": 75.84,
          "ProgramId": 204,
          "TaxRate": 192.34
        }
      ]
    },
    {
      "Id": 68,
      "Name": "Name4",
      "DiscountPercentage": 252.08,
      "SellOnline": false,
      "Services": [
        {
          "Price": 224.3,
          "OnlinePrice": 2.82,
          "TaxIncluded": 75.84,
          "ProgramId": 204,
          "TaxRate": 192.34
        },
        {
          "Price": 224.3,
          "OnlinePrice": 2.82,
          "TaxIncluded": 75.84,
          "ProgramId": 204,
          "TaxRate": 192.34
        }
      ]
    },
    {
      "Id": 68,
      "Name": "Name4",
      "DiscountPercentage": 252.08,
      "SellOnline": false,
      "Services": [
        {
          "Price": 224.3,
          "OnlinePrice": 2.82,
          "TaxIncluded": 75.84,
          "ProgramId": 204,
          "TaxRate": 192.34
        },
        {
          "Price": 224.3,
          "OnlinePrice": 2.82,
          "TaxIncluded": 75.84,
          "ProgramId": 204,
          "TaxRate": 192.34
        }
      ]
    }
  ],
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  }
}
```

