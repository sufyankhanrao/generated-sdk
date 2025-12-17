
# Get Active Clients Memberships Response

## Structure

`GetActiveClientsMembershipsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `client_memberships` | [`List[ClientMemberships]`](../../doc/models/client-memberships.md) | Optional | Details about the requested memberships. |

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
      "ClientId": "ClientId4",
      "Memberships": [
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
            },
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
          "IconCode": "IconCode0",
          "MembershipId": 132,
          "ActiveDate": "2016-03-13T12:52:32.123Z",
          "Count": 132
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
            },
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
          "IconCode": "IconCode0",
          "MembershipId": 132,
          "ActiveDate": "2016-03-13T12:52:32.123Z",
          "Count": 132
        }
      ],
      "ErrorMessage": "ErrorMessage0"
    },
    {
      "ClientId": "ClientId4",
      "Memberships": [
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
            },
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
          "IconCode": "IconCode0",
          "MembershipId": 132,
          "ActiveDate": "2016-03-13T12:52:32.123Z",
          "Count": 132
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
            },
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
          "IconCode": "IconCode0",
          "MembershipId": 132,
          "ActiveDate": "2016-03-13T12:52:32.123Z",
          "Count": 132
        }
      ],
      "ErrorMessage": "ErrorMessage0"
    }
  ]
}
```

