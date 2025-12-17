
# Waitlist Entry

## Structure

`WaitlistEntry`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `class_date` | `datetime` | Optional | The date of the class or enrollment. |
| `class_id` | `int` | Optional | The ID of the class or enrollment. |
| `class_schedule` | [`ClassSchedule`](../../doc/models/class-schedule.md) | Optional | Represents a single class instance. The class meets at the start time, goes until the end time. |
| `client` | [`Client`](../../doc/models/client.md) | Optional | The Client. |
| `enrollment_date_forward` | `datetime` | Optional | If the waiting list entry was created for an enrollment, this is the date on or after which the client can be added to the enrollment from the waitlist. |
| `id` | `int` | Optional | The ID of the waiting list entry. |
| `request_date_time` | `datetime` | Optional | The date and time that the request to be on the waiting list was made. |
| `visit_ref_no` | `int` | Optional | The ID of the visit that is associated with the waiting list entry. |
| `web` | `bool` | Optional | If `true`, the entry on the waiting list was requested online.<br /><br>If `false`, the entry on the waiting list was requested off-line, for example in person or by phone. |

## Example (as JSON)

```json
{
  "ClassDate": "2016-03-13T12:52:32.123Z",
  "ClassId": 26,
  "ClassSchedule": {
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
      },
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
    "Course": {
      "Id": 0,
      "Name": "Name6",
      "Description": "Description0",
      "Notes": "Notes2",
      "StartDate": "2016-03-13T12:52:32.123Z"
    },
    "SemesterId": 22,
    "IsAvailable": false
  },
  "Client": {
    "AppointmentGenderPreference": "None",
    "BirthDate": "2016-03-13T12:52:32.123Z",
    "Country": "Country8",
    "CreationDate": "2016-03-13T12:52:32.123Z",
    "CustomClientFields": [
      {
        "Value": "Value6",
        "Id": 112,
        "DataType": "DataType2",
        "Name": "Name8"
      }
    ]
  },
  "EnrollmentDateForward": "2016-03-13T12:52:32.123Z"
}
```

