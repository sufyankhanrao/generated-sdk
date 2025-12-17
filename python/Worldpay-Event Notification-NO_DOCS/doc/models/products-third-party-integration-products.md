
# Products Third Party Integration Products

Details of third party integration products

## Structure

`ProductsThirdPartyIntegrationProducts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_type` | [`ProductCodeShortLongDescription`](../../doc/models/product-code-short-long-description.md) | Optional | Information on the product type |
| `tier_levelcode` | [`TierLevelcodeEnum`](../../doc/models/tier-levelcode-enum.md) | Optional | code associated with the object<br><br>**Constraints**: *Maximum Length*: `1` |
| `tier_level_description` | [`TierLevelDescriptionEnum`](../../doc/models/tier-level-description-enum.md) | Optional | description associated with the object<br><br>**Constraints**: *Maximum Length*: `255` |
| `tier_changed_date` | `str` | Optional | Tier changed date<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `opt_in_date` | `str` | Optional | Opt in date<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |
| `opt_out_date` | `str` | Optional | Opt out date<br><br>**Constraints**: *Maximum Length*: `26`, *Pattern*: `[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}:[0-9]{6}` |

## Example (as JSON)

```json
{
  "tierLevelcode": "1",
  "tierLevelDescription": "ReviewTrackers",
  "productType": {
    "code": "code8",
    "shortDescription": "shortDescription4",
    "longDescription": "longDescription0"
  },
  "tierChangedDate": "tierChangedDate8",
  "optInDate": "optInDate2"
}
```

