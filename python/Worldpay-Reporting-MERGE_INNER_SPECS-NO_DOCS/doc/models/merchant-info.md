
# Merchant Info

Merchant information.

## Structure

`MerchantInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chain_code` | `str` | Optional | The Chain Code is the level of the merchant hierarchy that groups merchant identifiers (MIDs) and any related roll-up values under a common identifier for settlement, billing and reporting. Chain Code is the primary identifier for merchants boarded in MDB (Merchant Database) system.<br><br>**Constraints**: *Maximum Length*: `6` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `20` |
| `merchant_name` | `str` | Optional | Merchant Name refers to the name registered for businesses.<br><br>**Constraints**: *Maximum Length*: `50` |

## Example (as JSON)

```json
{
  "chainCode": "0F0086",
  "merchantId": "4445091191791",
  "merchantName": "HARPER ENGRAVING"
}
```

