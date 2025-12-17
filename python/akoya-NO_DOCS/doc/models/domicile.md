
# Domicile

The country and region of the business customer's location

*This model accepts additional fields of type Any.*

## Structure

`Domicile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `region` | `str` | Optional | - |
| `country` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example (as JSON)

```json
{
  "region": "region4",
  "country": "country2",
  "exampleAdditionalProperty": {
    "key1": "val1",
    "key2": "val2"
  }
}
```

