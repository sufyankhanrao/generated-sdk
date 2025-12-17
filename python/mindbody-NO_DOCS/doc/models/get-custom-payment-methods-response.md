
# Get Custom Payment Methods Response

## Structure

`GetCustomPaymentMethodsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `payment_methods` | [`List[CustomPaymentMethod]`](../../doc/models/custom-payment-method.md) | Optional | Contains information about the custom payment methods. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "PaymentMethods": [
    {
      "Id": 146,
      "Name": "Name0"
    }
  ]
}
```

