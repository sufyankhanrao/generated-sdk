
# Divisions for Patch Response

## Structure

`DivisionsForPatchResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `division` | [`Division`](../../doc/models/division.md) | Optional | - |
| `contact_data` | [`PrimaryContact`](../../doc/models/primary-contact.md) | Optional | - |
| `address_data` | [`PhysicalAddress`](../../doc/models/physical-address.md) | Optional | - |

## Example (as JSON)

```json
{
  "correlationId": "0acfc8fe1816421ab7376337d5729b94",
  "httpStatusCode": "200",
  "httpStatusMessage": "OK",
  "division": {
    "chainCode": "chainCode4",
    "divisionCode": "divisionCode0",
    "divisionName": "divisionName4"
  },
  "contactData": {
    "title": "title4",
    "firstName": "firstName4",
    "middleInitial": "middleInitial8",
    "lastName": "lastName4",
    "phoneNumber": "phoneNumber0",
    "phoneNumberExt": "phoneNumberExt0",
    "email": "email6"
  }
}
```

