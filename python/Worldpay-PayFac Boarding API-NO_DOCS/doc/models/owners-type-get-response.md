
# Owners Type Get Response

## Structure

`OwnersTypeGetResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `correlation_id` | `str` | Optional | guid sent in the httpheader v-correlation-id |
| `http_status_code` | `str` | Optional | - |
| `http_status_message` | `str` | Optional | - |
| `owner` | [`Owner`](../../doc/models/owner.md) | Optional | Owner of a Sub Merchant.<br><br>Please refer to the Beneficial Ownership section under Submerchant Boarding on the left hand side menu in the developer portal for specific requirements on Owner's SSN, DOB and other Owner attributes.They can be required based on Ownership Type and Ownership Percentage.<br>https://developerengine.fisglobal.com/apis/payfac#PFBeneficialOwners |

## Example (as JSON)

```json
{
  "correlationId": "correlationId2",
  "httpStatusCode": "httpStatusCode8",
  "httpStatusMessage": "httpStatusMessage2",
  "owner": {
    "title": "title0",
    "firstName": "firstName0",
    "middleInitial": "middleInitial2",
    "lastName": "lastName8",
    "phoneNumber": "phoneNumber6",
    "phoneNumberExt": "phoneNumberExt4",
    "faxNumber": "faxNumber8",
    "email": "email2",
    "ownershipPercentage": 1,
    "ssn": "ssn0",
    "addressLine1": "addressLine14",
    "city": "city6",
    "state": "WY",
    "country": "US",
    "postalCode": "postalCode4",
    "type": "BeneficialOwner3"
  }
}
```

