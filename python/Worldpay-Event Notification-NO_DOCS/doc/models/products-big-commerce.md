
# Products Big Commerce

Information on Big Commerce

## Structure

`ProductsBigCommerce`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `tier_levelcode` | [`TierLevelcodeEnum`](../../doc/models/tier-levelcode-enum.md) | Optional | code associated with the object<br><br>**Constraints**: *Maximum Length*: `1` |
| `tier_level_description` | [`TierLevelDescriptionEnum`](../../doc/models/tier-level-description-enum.md) | Optional | description associated with the object<br><br>**Constraints**: *Maximum Length*: `42` |
| `tier_changed_date` | `str` | Optional | Tier changed date<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `opt_in_date` | `str` | Optional | Opt in date<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `opt_out_date` | `str` | Optional | Opt out date<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `sku` | `str` | Optional | SKU<br><br>**Constraints**: *Maximum Length*: `255` |
| `service_code` | `str` | Optional | Service Code<br><br>**Constraints**: *Maximum Length*: `6` |

## Example (as JSON)

```json
{
  "tierLevelcode": "1",
  "tierLevelDescription": "Womply Bundled",
  "sku": "STORE-STANDARD-NP-MONTHLY",
  "serviceCode": "12345",
  "tierChangedDate": "tierChangedDate6",
  "optInDate": "optInDate0",
  "optOutDate": "optOutDate2"
}
```

