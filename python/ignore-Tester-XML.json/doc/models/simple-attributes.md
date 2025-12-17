
# Simple Attributes

A model with only attributes (attributes can only be non-array primitive types)

## Structure

`SimpleAttributes`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `string_element` | `str` | Required | string attribute (node name "string") |
| `nonreserved` | `str` | Required | string attribute (node name "nonreserved") |
| `number_element` | `int` | Required | number attribute (node name "number ") |
| `precision` | `float` | Required | precision attribute (node name "precision") |
| `boolean_element` | `bool` | Required | boolean attribute (node name "boolean") |
| `attributes_type` | `str` | Optional | - |

## Example (as XML)

```xml
<SimpleAttributes string="string-element6" nonreserved="nonreserved8" number="6" precision="28.62" boolean="false">
  <attributes_type>SimpleAttributes</attributes_type>
</SimpleAttributes>
```

