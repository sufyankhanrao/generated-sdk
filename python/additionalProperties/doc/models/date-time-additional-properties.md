
# Date Time Additional Properties

*This model accepts additional fields of type datetime.*

## Structure

`DateTimeAdditionalProperties`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `required_property` | `datetime` | Required | The required property |
| `additional_properties` | `Dict[str, datetime]` | Optional | - |

## Example (as JSON)

```json
{
  "requiredProperty": "2016-03-13T12:52:32.123Z",
  "exampleAdditionalProperty": "2016-03-13T12:52:32.123Z"
}
```

