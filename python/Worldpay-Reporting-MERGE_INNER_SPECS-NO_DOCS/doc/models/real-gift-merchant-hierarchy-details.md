
# Real Gift Merchant Hierarchy Details

Resource is used to retrieve gift transaction details for real time.

## Structure

`RealGiftMerchantHierarchyDetails`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `division_number` | `str` | Optional | The Division Number is a hierarchy level that enables merchants to roll-up child entities for Stores / Locations into different groups under a Chain. The Division Code is an optional hierarchy level but if created, is required for all child entities under the Division Number.<br><br>**Constraints**: *Maximum Length*: `3` |
| `store_number` | `str` | Optional | The Store/Location Code is the lowest roll-up level in the hierarchy system, grouping multiple merchant account numbers (MIDs) used in a single merchant location. The Store/ Locations are used to link multiple merchant numbers assigned to different terminals and/or business lines (MCC’s).<br><br>**Constraints**: *Maximum Length*: `9` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |
| `merchant_name` | `str` | Optional | Merchant Name refers to the name registered for businesses.<br><br>**Constraints**: *Maximum Length*: `50` |
| `clerk_id` | `str` | Optional | Indicates id of clerk<br><br>**Constraints**: *Maximum Length*: `9` |
| `mcc_code` | `str` | Optional | Merchant category codes (MCCs) are four-digit numbers that describe a merchant's primary business activities.<br><br>**Constraints**: *Maximum Length*: `4` |
| `terminal_capability` | [`CodeAndDescription1`](../../doc/models/code-and-description-1.md) | Optional | Refers to the code of terminal capabilities. |

## Example (as JSON)

```json
{
  "chainCode": "070110",
  "divisionNumber": "002",
  "storeNumber": "0001",
  "merchantId": "4445091034215",
  "merchantName": "CLIENT SERVICES TEST",
  "clerkId": "100728453",
  "mccCode": "5812",
  "terminalCapability": {
    "code": "0",
    "shortDescription": "UNKNOWN",
    "longDescription": "UNKNOWN"
  }
}
```

