
# Divisions for Patch

## Structure

`DivisionsForPatch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `division_name` | `str` | Optional | Division name for the division<br><br>**Constraints**: *Maximum Length*: `30` |
| `contact_data` | [`PrimaryContact`](../../doc/models/primary-contact.md) | Optional | - |
| `address_data` | [`PhysicalAddress`](../../doc/models/physical-address.md) | Optional | - |

## Example (as JSON)

```json
{
  "divisionName": "Division 001",
  "contactData": {
    "title": "title4",
    "firstName": "firstName4",
    "middleInitial": "middleInitial8",
    "lastName": "lastName4",
    "phoneNumber": "phoneNumber0",
    "phoneNumberExt": "phoneNumberExt0",
    "email": "email6"
  },
  "addressData": {
    "addressLine1": "addressLine14",
    "addressLine2": "addressLine22",
    "city": "city2",
    "state": "WI",
    "country": "US",
    "postalCode": "postalCode6",
    "postalCodeExtension": "postalCodeExtension0"
  }
}
```

