
# Base for Discriminator in Attribute

A model to serve as the base class for testing discriminator support using attributes.

## Structure

`BaseForDiscriminatorInAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `discriminator` | `str` | Optional | The discriminator attribute. |
| `base_field` | `str` | Required | String element in parent model. |

## Example (as XML)

```xml
<discriminated discrim="Darth Vader">
  <inherited>Base Field8</inherited>
</discriminated>
```

