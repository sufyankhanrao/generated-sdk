
# Simple Elements

A model with only non-array, primitive type elements. Look [here](https://gist.github.com/thehappybug/f6cf13f8b5c14a9079ed6402fffe6861#generate-simple-object) for the expected xml schema

## Structure

`SimpleElements`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `string_element` | `str` | Required | string element (element name "string") |
| `nonreserved` | `str` | Required | string element (element name "nonreserved") |
| `number_element` | `int` | Required | number element (element name "number ") |
| `precision` | `float` | Required | precision element (element name "precision") |
| `boolean_element` | `bool` | Required | boolean element (element name "boolean") |
| `model_type` | `str` | Optional | - |

## Example (as XML)

```xml
<SimpleElements>
  <model_type>SimpleElements</model_type>
  <string>string-element2</string>
  <nonreserved>nonreserved4</nonreserved>
  <number>150</number>
  <precision>22.38</precision>
  <boolean>false</boolean>
</SimpleElements>
```

