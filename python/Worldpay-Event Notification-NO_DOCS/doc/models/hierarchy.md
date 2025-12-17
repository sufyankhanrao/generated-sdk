
# Hierarchy

This aggregate field includes hierarchy data

## Structure

`Hierarchy`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sales_organization_code` | `str` | Optional | The identifier code that represents the entity value for the independent sales organization<br><br>**Constraints**: *Maximum Length*: `10` |
| `sales_organization_name` | `str` | Optional | The legal name of the independent sales organization<br><br>**Constraints**: *Maximum Length*: `30` |
| `sales_channel_code` | `str` | Optional | The identifier code that represents the entity value for the for the independent sales channel<br><br>**Constraints**: *Maximum Length*: `10` |
| `sales_channel_name` | `str` | Optional | The legal name of the independent sales channel<br><br>**Constraints**: *Maximum Length*: `30` |
| `partner_group_id` | `str` | Optional | The identifier associated with the partner group<br><br>**Constraints**: *Maximum Length*: `16` |
| `partner_group_name` | `str` | Optional | The legal name that represents the entity value for the partner group<br><br>**Constraints**: *Maximum Length*: `50` |
| `national_code` | `str` | Optional | The identifier code that represents the region where the business establishment is present<br><br>**Constraints**: *Maximum Length*: `7` |
| `national_name` | `str` | Optional | The legal name of the region where the business establishment is present<br><br>**Constraints**: *Maximum Length*: `30` |
| `super_chain_code` | `str` | Optional | TThe identifier code that represents the group of related chains of the partner<br><br>**Constraints**: *Maximum Length*: `10` |
| `super_chain_name` | `str` | Optional | The legal name that represents the group of related chains of the partner<br><br>**Constraints**: *Maximum Length*: `30` |
| `branch_code` | `str` | Optional | The identifier code that represents the entity value of the branch<br><br>**Constraints**: *Maximum Length*: `10` |
| `branch_name` | `str` | Optional | The legal name that represents the entity value of the branch<br><br>**Constraints**: *Maximum Length*: `30` |
| `division_code` | `str` | Optional | The Division Number is a hierarchy level that enables merchants to roll-up child entities for Stores / Locations into different groups under a Chain. The Division Code is an optional hierarchy level but if created, is required for all child entities under the Division Number.<br><br>**Constraints**: *Maximum Length*: `3` |
| `division_name` | `str` | Optional | The name associated with a given partner division<br><br>**Constraints**: *Maximum Length*: `30` |
| `chain_code` | `str` | Optional | The identifier code that represents the entity value of the chain<br><br>**Constraints**: *Maximum Length*: `6` |
| `chain_name` | `str` | Optional | The legal name that represents the entity value for the chain<br><br>**Constraints**: *Maximum Length*: `25` |
| `store_number` | `str` | Optional | The identifier code of a store under a given partner chain. Can store alphanumber value when creating the store<br><br>**Constraints**: *Maximum Length*: `9` |
| `store_name` | `str` | Optional | The legal name that represents the entity value for the store<br><br>**Constraints**: *Maximum Length*: `40` |
| `merchant_id` | `str` | Optional | The Merchant hierarchy level is the last level in the Vertical Hierarchy. MID is the unique identifier assigned for a processing location, business type, MCC Code that requires a specific value to define merchant authorizations, settlement, reporting, pricing and billing levels.<br><br>**Constraints**: *Maximum Length*: `10` |
| `merchant_name` | `str` | Optional | The legal name that represents the entity value for the merchant<br><br>**Constraints**: *Maximum Length*: `30` |

## Example (as JSON)

```json
{
  "salesOrganizationCode": "12",
  "salesOrganizationName": "ABCD",
  "salesChannelCode": "73",
  "salesChannelName": "VANT",
  "partnerGroupId": "41",
  "partnerGroupName": "VANT",
  "nationalCode": "NATNL",
  "nationalName": "ABC Bank",
  "superChainCode": "DA012",
  "superChainName": "ABC CORP",
  "branchCode": "9999",
  "branchName": "SAP 123",
  "divisionCode": "DIV",
  "divisionName": "My division Name",
  "chainCode": "0X1234",
  "chainName": "My Chain Name",
  "storeNumber": "000000001",
  "storeName": "My Store Name",
  "merchantId": "1234567890",
  "merchantName": "Merchant Name"
}
```

