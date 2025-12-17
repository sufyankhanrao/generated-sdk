
# Get Waitlist Entries Response

## Structure

`GetWaitlistEntriesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pagination_response` | [`PaginationResponse`](../../doc/models/pagination-response.md) | Optional | Contains information about the pagination to use. |
| `waitlist_entries` | [`List[WaitlistEntry]`](../../doc/models/waitlist-entry.md) | Optional | Contains information about the waiting list entries. |

## Example (as JSON)

```json
{
  "PaginationResponse": {
    "RequestedLimit": 22,
    "RequestedOffset": 0,
    "PageSize": 172,
    "TotalResults": 112
  },
  "WaitlistEntries": [
    {
      "ClassDate": "2016-03-13T12:52:32.123Z",
      "ClassId": 62,
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
    },
    {
      "ClassDate": "2016-03-13T12:52:32.123Z",
      "ClassId": 62,
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
  ]
}
```

