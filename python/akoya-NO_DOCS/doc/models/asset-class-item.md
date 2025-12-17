
# Asset Class Item

*This model accepts additional fields of type Any.*

## Structure

`AssetClassItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `asset_class` | [`AssetClass`](../../doc/models/asset-class.md) | Optional | - |
| `percent` | `float` | Optional | Percentage of asset class that falls under this asset |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "assetClass": "INTLSTOCK",
  "percent": 129.54,
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

