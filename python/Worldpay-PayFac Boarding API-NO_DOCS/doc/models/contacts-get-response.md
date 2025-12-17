
# Contacts Get Response

## Structure

`ContactsGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `contacts` | [`List[Contact]`](../../doc/models/contact.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "contacts": [
    {
      "title": "title4",
      "firstName": "firstName6",
      "middleInitial": "middleInitial6",
      "lastName": "lastName2",
      "phoneNumber": "phoneNumber2",
      "phoneNumberExt": "phoneNumberExt8",
      "email": "email8",
      "faxNumber": "faxNumber2",
      "type": "Primary"
    },
    {
      "title": "title4",
      "firstName": "firstName6",
      "middleInitial": "middleInitial6",
      "lastName": "lastName2",
      "phoneNumber": "phoneNumber2",
      "phoneNumberExt": "phoneNumberExt8",
      "email": "email8",
      "faxNumber": "faxNumber2",
      "type": "Primary"
    }
  ]
}
```

