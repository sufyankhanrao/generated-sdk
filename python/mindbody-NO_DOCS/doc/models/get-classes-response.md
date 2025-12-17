
# Get Classes Response

## Structure

`GetClassesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `classes` | [`List[Class]`](../../doc/models/class.md) | Optional | A list of the requested classes. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "Classes": [
    {
      "ClassScheduleId": 50,
      "Visits": [
        {
          "AppointmentId": 196,
          "AppointmentGenderPreference": "Male",
          "AppointmentStatus": "Booked",
          "ClassId": 140,
          "ClientId": "ClientId4"
        },
        {
          "AppointmentId": 196,
          "AppointmentGenderPreference": "Male",
          "AppointmentStatus": "Booked",
          "ClassId": 140,
          "ClientId": "ClientId4"
        }
      ],
      "Clients": [
        {
          "AppointmentGenderPreference": "Female",
          "BirthDate": "2016-03-13T12:52:32.123Z",
          "Country": "Country4",
          "CreationDate": "2016-03-13T12:52:32.123Z",
          "CustomClientFields": [
            {
              "Value": "Value6",
              "Id": 112,
              "DataType": "DataType2",
              "Name": "Name8"
            },
            {
              "Value": "Value6",
              "Id": 112,
              "DataType": "DataType2",
              "Name": "Name8"
            }
          ]
        }
      ],
      "Location": {
        "AdditionalImageURLs": [
          "AdditionalImageURLs4"
        ],
        "Address": "Address2",
        "Address2": "Address24",
        "Amenities": [
          {
            "Id": 214,
            "Name": "Name8"
          },
          {
            "Id": 214,
            "Name": "Name8"
          },
          {
            "Id": 214,
            "Name": "Name8"
          }
        ],
        "BusinessDescription": "BusinessDescription8"
      },
      "Resource": {
        "Id": 22,
        "Name": "Name6"
      }
    },
    {
      "ClassScheduleId": 50,
      "Visits": [
        {
          "AppointmentId": 196,
          "AppointmentGenderPreference": "Male",
          "AppointmentStatus": "Booked",
          "ClassId": 140,
          "ClientId": "ClientId4"
        },
        {
          "AppointmentId": 196,
          "AppointmentGenderPreference": "Male",
          "AppointmentStatus": "Booked",
          "ClassId": 140,
          "ClientId": "ClientId4"
        }
      ],
      "Clients": [
        {
          "AppointmentGenderPreference": "Female",
          "BirthDate": "2016-03-13T12:52:32.123Z",
          "Country": "Country4",
          "CreationDate": "2016-03-13T12:52:32.123Z",
          "CustomClientFields": [
            {
              "Value": "Value6",
              "Id": 112,
              "DataType": "DataType2",
              "Name": "Name8"
            },
            {
              "Value": "Value6",
              "Id": 112,
              "DataType": "DataType2",
              "Name": "Name8"
            }
          ]
        }
      ],
      "Location": {
        "AdditionalImageURLs": [
          "AdditionalImageURLs4"
        ],
        "Address": "Address2",
        "Address2": "Address24",
        "Amenities": [
          {
            "Id": 214,
            "Name": "Name8"
          },
          {
            "Id": 214,
            "Name": "Name8"
          },
          {
            "Id": 214,
            "Name": "Name8"
          }
        ],
        "BusinessDescription": "BusinessDescription8"
      },
      "Resource": {
        "Id": 22,
        "Name": "Name6"
      }
    }
  ]
}
```

