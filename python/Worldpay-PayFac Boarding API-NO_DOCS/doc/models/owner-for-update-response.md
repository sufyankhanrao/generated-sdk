
# Owner for Update Response

## Structure

`OwnerForUpdateResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `owner` | [`List[OwnerUpdated]`](../../doc/models/owner-updated.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId6",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "owner": [
    {
      "title": "title0",
      "firstName": "firstName0",
      "middleInitial": "middleInitial2",
      "lastName": "lastName8",
      "phoneNumber": "phoneNumber6",
      "phoneNumberExt": "phoneNumberExt4",
      "faxNumber": "faxNumber8",
      "addressLine1": "addressLine14",
      "city": "city6",
      "state": "WY",
      "country": "US",
      "postalCode": "postalCode4"
    }
  ]
}
```

