
# Owners Get Response

## Structure

`OwnersGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `owners` | [`List[Owner]`](../../doc/models/owner.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "correlationId4",
  "httpStatusCode": "httpStatusCode0",
  "httpStatusMessage": "httpStatusMessage4",
  "owners": [
    {
      "title": "title0",
      "firstName": "firstName0",
      "middleInitial": "middleInitial2",
      "lastName": "lastName8",
      "phoneNumber": "phoneNumber6",
      "phoneNumberExt": "phoneNumberExt4",
      "faxNumber": "faxNumber8",
      "email": "email2",
      "ownershipPercentage": 100,
      "ssn": "ssn0",
      "addressLine1": "addressLine16",
      "city": "city4",
      "state": "GA",
      "country": "US",
      "postalCode": "postalCode4",
      "type": "BeneficialOwner4"
    }
  ]
}
```

