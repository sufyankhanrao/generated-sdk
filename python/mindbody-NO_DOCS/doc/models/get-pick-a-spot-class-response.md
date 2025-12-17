
# Get Pick a Spot Class Response

Contains information about the get PickASpot class response.

## Structure

`GetPickASpotClassResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classes` | [`List[PickASpotClass]`](../../doc/models/pick-a-spot-class.md) | Optional | Contains information about the PickASpot classes. |
| `pagination` | [`Pagination`](../../doc/models/pagination.md) | Optional | Contains information about the pagination used. |
| `response_details` | [`ResponseDetails`](../../doc/models/response-details.md) | Optional | Contains information about the response message detail. |

## Example (as JSON)

```json
{
  "classes": [
    {
      "SiteId": 100,
      "LocationId": 14,
      "ClassId": "ClassId4",
      "ClassExternalId": "ClassExternalId6",
      "ClassName": "ClassName2"
    },
    {
      "SiteId": 100,
      "LocationId": 14,
      "ClassId": "ClassId4",
      "ClassExternalId": "ClassExternalId6",
      "ClassName": "ClassName2"
    },
    {
      "SiteId": 100,
      "LocationId": 14,
      "ClassId": "ClassId4",
      "ClassExternalId": "ClassExternalId6",
      "ClassName": "ClassName2"
    }
  ],
  "pagination": {
    "PageNumber": 92,
    "PageSize": 26,
    "TotalResultCount": 42,
    "TotalPageCount": 112
  },
  "responseDetails": {
    "Status": "Status8",
    "TransactionId": "TransactionId8",
    "Message": "Message6"
  }
}
```

