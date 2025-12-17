
# Get Client Complete Info Response

Contains information about the requested client.

## Structure

`GetClientCompleteInfoResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client` | [`ClientWithSuspensionInfo`](../../doc/models/client-with-suspension-info.md) | Optional | A Client DTO with Suspension Informatoin |
| `client_services` | [`List[ClientService]`](../../doc/models/client-service.md) | Optional | Contains information about client pricing options. |
| `client_contracts` | [`List[ClientContract]`](../../doc/models/client-contract.md) | Optional | Contains information about client contract. |
| `client_memberships` | [`List[ClientMembership]`](../../doc/models/client-membership.md) | Optional | Contains information about client Memberships. |
| `client_arrivals` | [`List[ClientArrival]`](../../doc/models/client-arrival.md) | Optional | Contains information about client arrival services. |

## Example (as JSON)

```json
{
  "Client": {
    "SuspensionInfo": {
      "BookingSuspended": false,
      "SuspensionStartDate": "SuspensionStartDate8",
      "SuspensionEndDate": "SuspensionEndDate2"
    },
    "AppointmentGenderPreference": "None",
    "BirthDate": "2016-03-13T12:52:32.123Z",
    "Country": "Country8",
    "CreationDate": "2016-03-13T12:52:32.123Z"
  },
  "ClientServices": [
    {
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 38,
      "Current": false,
      "ExpirationDate": "2016-03-13T12:52:32.123Z",
      "Id": 230
    },
    {
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 38,
      "Current": false,
      "ExpirationDate": "2016-03-13T12:52:32.123Z",
      "Id": 230
    },
    {
      "ActiveDate": "2016-03-13T12:52:32.123Z",
      "Count": 38,
      "Current": false,
      "ExpirationDate": "2016-03-13T12:52:32.123Z",
      "Id": 230
    }
  ],
  "ClientContracts": [
    {
      "AgreementDate": "2016-03-13T12:52:32.123Z",
      "AutopayStatus": "Active",
      "ContractName": "ContractName4",
      "EndDate": "2016-03-13T12:52:32.123Z",
      "Id": 178
    }
  ],
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
    }
  ],
  "ClientArrivals": [
    {
      "ArrivalProgramID": 48,
      "ArrivalProgramName": "ArrivalProgramName4",
      "CanAccess": false,
      "LocationsIDs": [
        71
      ]
    },
    {
      "ArrivalProgramID": 48,
      "ArrivalProgramName": "ArrivalProgramName4",
      "CanAccess": false,
      "LocationsIDs": [
        71
      ]
    },
    {
      "ArrivalProgramID": 48,
      "ArrivalProgramName": "ArrivalProgramName4",
      "CanAccess": false,
      "LocationsIDs": [
        71
      ]
    }
  ]
}
```

