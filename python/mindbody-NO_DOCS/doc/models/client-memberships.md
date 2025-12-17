
# Client Memberships

## Structure

`ClientMemberships`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_id` | `str` | Optional | ID of the client. |
| `memberships` | [`List[ClientMembership]`](../../doc/models/client-membership.md) | Optional | Contains information about the Client Memberships details. |
| `error_message` | `str` | Optional | - |

## Example (as JSON)

```json
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
```

