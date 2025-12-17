
# Class Schedule

Represents a single class instance. The class meets at the start time, goes until the end time.

## Structure

`ClassSchedule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `classes` | [`List[Class]`](../../doc/models/class.md) | Optional | Contains information about a class. |
| `clients` | [`List[Client]`](../../doc/models/client.md) | Optional | Contains information about clients. |
| `course` | [`Course`](../../doc/models/course.md) | Optional | A course. |
| `semester_id` | `int` | Optional | The semester ID for the enrollment (if any). |
| `is_available` | `bool` | Optional | When `true`, indicates that the enrollment shows in consumer mode, has not started yet, and there is room in each class of the enrollment.<br /><br>When `false`, indicates that either the enrollment does not show in consumer mode, has already started, or there is no room in some classes of the enrollment. |
| `id` | `int` | Optional | The unique ID of the class schedule. |
| `class_description` | [`ClassDescription`](../../doc/models/class-description.md) | Optional | Represents a class definition. The class meets at the start time, goes until the end time. |
| `day_sunday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Sundays. |
| `day_monday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Mondays. |
| `day_tuesday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Tuesdays. |
| `day_wednesday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Wednesdays. |
| `day_thursday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Thursdays. |
| `day_friday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Fridays. |
| `day_saturday` | `bool` | Optional | When `true`, indicates that this schedule occurs on Saturdays. |
| `allow_open_enrollment` | `bool` | Optional | When `true`, indicates that the enrollment allows booking after the enrollment has started. |
| `allow_date_forward_enrollment` | `bool` | Optional | When `true`, indicates that this the enrollment shows in consumer mode, the enrollment has not started yet, and there is room in each class of the enrollment. |
| `start_time` | `datetime` | Optional | The time this class schedule starts. |
| `end_time` | `datetime` | Optional | The time this class schedule ends. |
| `start_date` | `datetime` | Optional | The date this class schedule starts. |
| `end_date` | `datetime` | Optional | The date this class schedule ends. |
| `staff` | [`Staff`](../../doc/models/staff.md) | Optional | The Staff |
| `location` | [`Location`](../../doc/models/location.md) | Optional | - |
| `frequency_type` | [`FrequencyTypeEnum`](../../doc/models/frequency-type-enum.md) | Optional | The class schedule recurrence type. |
| `frequency_interval` | `int` | Optional | The interval between class schedule occurencies. |

## Example (as JSON)

```json
{
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
}
```

