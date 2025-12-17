
# UUID Additional Properties

*This model accepts additional fields of type uuid|str.*

## Structure

`UUIDAdditionalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_property` | `uuid\|str` | Required | The required property |
| `additional_properties` | `Dict[str, uuid\|str]` | Optional | - |

## Example (as JSON)

```json
{
  "requiredProperty": "00002024-0000-0000-0000-000000000000",
  "exampleAdditionalProperty": "0000224f-0000-0000-0000-000000000000"
}
```

