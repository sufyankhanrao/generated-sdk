
# Gift Merchant Hierarchy Details 1

Refers to gift details

## Structure

`GiftMerchantHierarchyDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `store_number` | `str` | Optional | The Store/Location Code is the lowest roll-up level in the hierarchy system, grouping multiple merchant account numbers (MIDs) used in a single merchant location. The Store/ Locations are used to link multiple merchant numbers assigned to different terminals and/or business lines (MCC’s).<br><br>**Constraints**: *Maximum Length*: `9` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |
| `alternate_merchant_id` | `str` | Optional | Merchant level is lowest level in the FIS Merchant Hierarchy structure. Merchant ID (MID) is a 12-16 digit unique identifier assigned to each Merchant<br><br>**Constraints**: *Maximum Length*: `16` |

## Example (as JSON)

```json
{
  "storeNumber": "0001",
  "merchantId": "4445091034215",
  "alternateMerchantId": "521110665864"
}
```

