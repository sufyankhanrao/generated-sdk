
# Model With Nested Attributes Model

## Structure

`ModelWithNestedAttributesModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `simple_attributes` | [`SimpleAttributes`](../../doc/models/simple-attributes.md) | Required | A model with only attributes (attributes can only be non-array primitive types) |
| `simple` | `str` | Required | - |

## Example (as XML)

```xml
<ModelWithNestedAttributesModel>
  <Attributes string="string-element6" nonreserved="nonreserved8" number="6" precision="28.62" boolean="false">
    <attributes_type>SimpleAttributes</attributes_type>
  </Attributes>
  <simple>simple8</simple>
</ModelWithNestedAttributesModel>
```

