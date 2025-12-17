
# Bank Card Merchant Hierarchy Detail

## Structure

`BankCardMerchantHierarchyDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `division_number` | `str` | Optional | The Division is a hierarchy level that enables merchants to roll-up child entities for Stores / Locations into different groups under a Chain. It is an optional hierarchy level but if created, is required for all child entities under the Division Number which is typically 3 digits and unique to that particular Chain meaning same Division number can exist for a Division under a different Chain but no duplicates are allowed under the same Chain.<br><br>**Constraints**: *Maximum Length*: `3` |
| `store_number` | `str` | Optional | The Store/Location is the lowest roll-up level in the hierarchy system, grouping multiple merchant account numbers (MIDs) used in a single merchant location assigned to different terminals and/or business lines (MCC’s). A Store Number is of 9 digits and unique to a particular Chain meaning same Store Number can exist for a Store under a different Divison/Chain but no duplicates under the same Divison/Chain.<br><br>**Constraints**: *Maximum Length*: `9` |
| `merchant_id` | `str` | Optional | Merchant level is lowest level in the FIS Merchant Hierarchy structure. Merchant ID (MID) is a 12-16 digit unique identifier assigned to each Merchant which is used to identify a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |

## Example (as JSON)

```json
{
  "chainCode": "070110",
  "divisionNumber": "002",
  "storeNumber": "000000001",
  "merchantId": "4445091191791"
}
```

