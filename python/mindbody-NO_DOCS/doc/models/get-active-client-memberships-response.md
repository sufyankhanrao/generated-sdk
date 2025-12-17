
# Get Active Client Memberships Response

## Structure

`GetActiveClientMembershipsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `client_memberships` | [`List[ClientMembership]`](../../doc/models/client-membership.md) | Optional | Details about the requested memberships. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "ClientMemberships": [
    {
      "RestrictedLocations": [
        {
          "AdditionalImageURLs": [
            "AdditionalImageURLs0",
            "AdditionalImageURLs9"
          ],
          "Address": "Address4",
          "Address2": "Address26",
          "Amenities": [
            {
              "Id": 214,
              "Name": "Name8"
            },
            {
              "Id": 214,
              "Name": "Name8"
            }
          ],
          "BusinessDescription": "BusinessDescription0"
        }
      ],
      "IconCode": "IconCode6",
      "MembershipId": 22,
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 22
    },
    {
      "RestrictedLocations": [
        {
          "AdditionalImageURLs": [
            "AdditionalImageURLs0",
            "AdditionalImageURLs9"
          ],
          "Address": "Address4",
          "Address2": "Address26",
          "Amenities": [
            {
              "Id": 214,
              "Name": "Name8"
            },
            {
              "Id": 214,
              "Name": "Name8"
            }
          ],
          "BusinessDescription": "BusinessDescription0"
        }
      ],
      "IconCode": "IconCode6",
      "MembershipId": 22,
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 22
    },
    {
      "RestrictedLocations": [
        {
          "AdditionalImageURLs": [
            "AdditionalImageURLs0",
            "AdditionalImageURLs9"
          ],
          "Address": "Address4",
          "Address2": "Address26",
          "Amenities": [
            {
              "Id": 214,
              "Name": "Name8"
            },
            {
              "Id": 214,
              "Name": "Name8"
            }
          ],
          "BusinessDescription": "BusinessDescription0"
        }
      ],
      "IconCode": "IconCode6",
      "MembershipId": 22,
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 22
    }
  ]
}
```

