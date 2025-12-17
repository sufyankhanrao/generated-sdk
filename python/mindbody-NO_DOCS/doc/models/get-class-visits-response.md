
# Get Class Visits Response

## Structure

`GetClassVisitsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mclass` | [`Class`](../../doc/models/class.md) | Optional | Represents a single class instance. The class meets at the start time, goes until the end time. |

## Example (as JSON)

```json
{
  "Class": {
    "ClassScheduleId": 206,
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
}
```

