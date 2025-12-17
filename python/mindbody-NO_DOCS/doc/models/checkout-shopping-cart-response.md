
# Checkout Shopping Cart Response

## Structure

`CheckoutShoppingCartResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `shopping_cart` | [`ShoppingCart`](../../doc/models/shopping-cart.md) | Optional | - |
| `classes` | [`List[Class]`](../../doc/models/class.md) | Optional | Contains information about the classes. |
| `appointments` | [`List[Appointment]`](../../doc/models/appointment.md) | Optional | Contains information about the appointments. |
| `enrollments` | [`List[ClassSchedule]`](../../doc/models/class-schedule.md) | Optional | Contains information about enrollment class schedules. |

## Example (as JSON)

```json
{
  "ShoppingCart": {
    "Id": "Id0",
    "CartItems": [
      {
        "Item": {
          "key1": "val1",
          "key2": "val2"
        },
        "DiscountAmount": 4.36,
        "VisitIds": [
          232,
          233
        ],
        "AppointmentIds": [
          98
        ],
        "Appointments": [
          {
            "GenderPreference": "None",
            "Duration": 20,
            "ProviderId": "ProviderId8",
            "Id": 230,
            "Status": "Completed"
          },
          {
            "GenderPreference": "None",
            "Duration": 20,
            "ProviderId": "ProviderId8",
            "Id": 230,
            "Status": "Completed"
          }
        ]
      },
      {
        "Item": {
          "key1": "val1",
          "key2": "val2"
        },
        "DiscountAmount": 4.36,
        "VisitIds": [
          232,
          233
        ],
        "AppointmentIds": [
          98
        ],
        "Appointments": [
          {
            "GenderPreference": "None",
            "Duration": 20,
            "ProviderId": "ProviderId8",
            "Id": 230,
            "Status": "Completed"
          },
          {
            "GenderPreference": "None",
            "Duration": 20,
            "ProviderId": "ProviderId8",
            "Id": 230,
            "Status": "Completed"
          }
        ]
      },
      {
        "Item": {
          "key1": "val1",
          "key2": "val2"
        },
        "DiscountAmount": 4.36,
        "VisitIds": [
          232,
          233
        ],
        "AppointmentIds": [
          98
        ],
        "Appointments": [
          {
            "GenderPreference": "None",
            "Duration": 20,
            "ProviderId": "ProviderId8",
            "Id": 230,
            "Status": "Completed"
          },
          {
            "GenderPreference": "None",
            "Duration": 20,
            "ProviderId": "ProviderId8",
            "Id": 230,
            "Status": "Completed"
          }
        ]
      }
    ],
    "SubTotal": 108.54,
    "DiscountTotal": 99.92,
    "TaxTotal": 136.36
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
  "Appointments": [
    {
      "GenderPreference": "None",
      "Duration": 20,
      "ProviderId": "ProviderId8",
      "Id": 230,
      "Status": "Completed"
    }
  ],
  "Enrollments": [
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
      "Course": {
        "Id": 0,
        "Name": "Name6",
        "Description": "Description0",
        "Notes": "Notes2",
        "StartDate": "2016-03-13T12:52:32.123Z"
      },
      "SemesterId": 42,
      "IsAvailable": false
    },
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
      "Course": {
        "Id": 0,
        "Name": "Name6",
        "Description": "Description0",
        "Notes": "Notes2",
        "StartDate": "2016-03-13T12:52:32.123Z"
      },
      "SemesterId": 42,
      "IsAvailable": false
    },
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
      "Course": {
        "Id": 0,
        "Name": "Name6",
        "Description": "Description0",
        "Notes": "Notes2",
        "StartDate": "2016-03-13T12:52:32.123Z"
      },
      "SemesterId": 42,
      "IsAvailable": false
    }
  ]
}
```

