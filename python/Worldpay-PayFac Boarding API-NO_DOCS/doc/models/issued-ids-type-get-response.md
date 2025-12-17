
# Issued Ids Type Get Response

## Structure

`IssuedIdsTypeGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `issued_id` | [`IssuedId`](../../doc/models/issued-id.md) | Optional | Id Verification for the  Owners |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "issuedId": {
    "idNumber": "idNumber2",
    "issuedCity": "issuedCity8",
    "issuedState": "MO",
    "issuedCountry": "US",
    "dateIssued": "2016-03-13",
    "dateExpires": "2016-03-13",
    "idType": "Other"
  }
}
```

