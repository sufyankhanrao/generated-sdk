
# Customer Price List Response

## Structure

`CustomerPriceListResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | UUID (according to RFC 4122 standards) for requests and responses. This will be played back in the response from the request. |
| `price_list` | [`List[PriceList]`](../../doc/models/price-list.md) | Optional | - |
| `error` | [`ErrorStatus`](../../doc/models/error-status.md) | Optional | - |

## Example (as JSON)

```json
{
  "RequestId": "RequestId0",
  "PriceList": [
    {
      "Date": "Date8",
      "Day": "Day4",
      "Type": "Type0",
      "PriceListId": 210,
      "PriceListDescription": "PriceListDescription0"
    },
    {
      "Date": "Date8",
      "Day": "Day4",
      "Type": "Type0",
      "PriceListId": 210,
      "PriceListDescription": "PriceListDescription0"
    },
    {
      "Date": "Date8",
      "Day": "Day4",
      "Type": "Type0",
      "PriceListId": 210,
      "PriceListDescription": "PriceListDescription0"
    }
  ],
  "Error": {
    "Code": "Code4",
    "Description": "Description2"
  }
}
```

