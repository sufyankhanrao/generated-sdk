
# Debit Merchant Hierarchy Details 1

This object provides details of transaction location -- merchant related information

## Structure

`DebitMerchantHierarchyDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `acro` | `str` | Optional | Each hierarchy has a generic ACRO defined by default per banking relationship.All merchants have a 4 character billing acronym.<br><br>**Constraints**: *Maximum Length*: `4` |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `division_number` | `str` | Optional | The Division Number is a hierarchy level that enables merchants to roll-up child entities for Stores / Locations into different groups under a Chain. The Division Code is an optional hierarchy level but if created, is required for all child entities under the Division Number.<br><br>**Constraints**: *Maximum Length*: `3` |
| `store_number` | `str` | Optional | The Store/Location is the lowest roll-up level in the hierarchy system, grouping multiple merchant account numbers (MIDs) used in a single merchant location assigned to different terminals and/or business lines (MCC’s). A Store Number is of 9 digits and unique to a particular Chain meaning same Store Number can exist for a Store under a different Divison/Chain but no duplicates under the same Divison/Chain.<br><br>**Constraints**: *Maximum Length*: `9` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |
| `merchant_name` | `str` | Optional | Merchant Name refers to the name registered for the business.<br><br>**Constraints**: *Maximum Length*: `256` |

## Example (as JSON)

```json
{
  "acro": "WALG",
  "chainCode": "070110",
  "divisionNumber": "088",
  "storeNumber": "000000001",
  "merchantId": "4445091034215",
  "merchantName": "CLIENT SERVICES TEST"
}
```

