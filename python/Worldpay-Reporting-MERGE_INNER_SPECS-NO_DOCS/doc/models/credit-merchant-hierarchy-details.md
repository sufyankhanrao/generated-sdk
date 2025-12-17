
# Credit Merchant Hierarchy Details

This object provides details of transaction location -- merchant related information

## Structure

`CreditMerchantHierarchyDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `store_number` | `str` | Optional | The Store/Location is the lowest roll-up level in the hierarchy system, grouping multiple merchant account numbers (MIDs) used in a single merchant location assigned to different terminals and/or business lines (MCC’s). A Store Number is of 9 digits and unique to a particular Chain meaning same Store Number can exist for a Store under a different Divison/Chain but no duplicates under the same Divison/Chain.<br><br>**Constraints**: *Maximum Length*: `9` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |
| `alternate_merchant_id` | `str` | Optional | Merchant level is lowest level in the FIS Merchant Hierarchy structure. Merchant ID (MID) is a 12-16 digit unique identifier assigned to each Merchant<br><br>**Constraints**: *Maximum Length*: `16` |
| `merchant_name` | `str` | Optional | Merchant Name refers to the name registered for the business.<br><br>**Constraints**: *Maximum Length*: `256` |
| `employee_number` | `int` | Optional | Refers to one of the following sales person/clerk id/ employee number<br><br>**Constraints**: `>= 9`, `<= 9` |

## Example (as JSON)

```json
{
  "storeNumber": "000000001",
  "merchantId": "444512303421535",
  "alternateMerchantId": "521110665864",
  "merchantName": "CLIENT SERVICES TEST",
  "employeeNumber": 9
}
```

