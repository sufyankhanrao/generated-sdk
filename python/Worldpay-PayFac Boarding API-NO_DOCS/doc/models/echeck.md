
# Echeck

## Structure

`Echeck`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enable_echeck` | `bool` | Required | - |
| `transaction_thresholds` | [`EcheckTransactionThresholds`](../../doc/models/echeck-transaction-thresholds.md) | Required | Transaction thresholds for eCheck processing |
| `principal_signer` | [`PrincipalSigner`](../../doc/models/principal-signer.md) | Optional | Principal Signer for eCheck.This information is "required" for the Signer of the ACH Merchant Agreement to satisfy KYC regulations. If you do not complete these fields, your ACH Merchant Account may be subject to suspension. If you have any questions or concerns, please contact your Relationship Manager. |

## Example (as JSON)

```json
{
  "enableEcheck": false,
  "transactionThresholds": {
    "singleTransactionAmount": 156,
    "dailyTransactionCount": 110,
    "dailyTransactionAmount": 16,
    "monthlyTransactionCount": 58,
    "monthlyTransactionAmount": 224,
    "perCustomer": {
      "dailyTransactionCount": 132,
      "dailyTransactionAmount": 6,
      "dailyTransactionDeclineCount": 248
    }
  },
  "principalSigner": {
    "title": "title0",
    "firstName": "firstName0",
    "middleInitial": "middleInitial2",
    "lastName": "lastName8",
    "dob": "2016-03-13",
    "ownershipPercentage": 52,
    "email": "email2",
    "addressLine1": "addressLine16",
    "addressLine2": "addressLine24",
    "city": "city6",
    "state": "WY",
    "country": "US",
    "postalCode": "postalCode4",
    "postalCodeExtension": "postalCodeExtension8",
    "phoneNumber": "phoneNumber6",
    "phoneNumberExt": "phoneNumberExt4",
    "ssn": "ssn0"
  }
}
```

