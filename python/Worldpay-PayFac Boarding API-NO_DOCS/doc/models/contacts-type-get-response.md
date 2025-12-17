
# Contacts Type Get Response

## Structure

`ContactsTypeGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `contact` | [`Contact`](../../doc/models/contact.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "contact": {
    "title": "title8",
    "firstName": "firstName2",
    "middleInitial": "middleInitial0",
    "lastName": "lastName6",
    "phoneNumber": "phoneNumber2",
    "phoneNumberExt": "phoneNumberExt2",
    "email": "email4",
    "faxNumber": "faxNumber6",
    "type": "TerminalDeployment"
  }
}
```

