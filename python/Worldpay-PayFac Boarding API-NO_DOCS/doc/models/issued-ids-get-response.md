
# Issued Ids Get Response

## Structure

`IssuedIdsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `issued_ids` | [`List[IssuedId]`](../../doc/models/issued-id.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "issuedIds": [
    {
      "idNumber": "idNumber2",
      "issuedCity": "issuedCity8",
      "issuedState": "QC",
      "issuedCountry": "US",
      "dateIssued": "2016-03-13",
      "dateExpires": "2016-03-13",
      "idType": "MexicanConsulate"
    },
    {
      "idNumber": "idNumber2",
      "issuedCity": "issuedCity8",
      "issuedState": "QC",
      "issuedCountry": "US",
      "dateIssued": "2016-03-13",
      "dateExpires": "2016-03-13",
      "idType": "MexicanConsulate"
    }
  ]
}
```

