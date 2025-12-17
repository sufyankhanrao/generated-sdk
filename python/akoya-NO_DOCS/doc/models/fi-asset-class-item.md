
# Fi Asset Class Item

*This model accepts additional fields of type Any.*

## Structure

`FiAssetClassItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_class` | `str` | Optional | FI-specific asset class |
| `percent` | `float` | Optional | Percentage of asset class that falls under this asset |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "assetClass": "assetClass8",
  "percent": 83.14,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

