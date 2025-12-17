
# Issued Ids Post Response

## Structure

`IssuedIdsPostResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `issued_ids` | [`List[IssuedIdPosted]`](../../doc/models/issued-id-posted.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId0",
  "httpStatusCode": "httpStatusCode6",
  "httpStatusMessage": "httpStatusMessage0",
  "issuedIds": [
    {
      "idNumber": "idNumber2",
      "issuedCity": "issuedCity8",
      "issuedState": "QC",
      "issuedCountry": "US",
      "dateIssued": "2016-03-13",
      "dateExpires": "2016-03-13"
    }
  ]
}
```

