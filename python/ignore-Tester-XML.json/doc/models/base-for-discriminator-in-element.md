
# Base for Discriminator in Element

A model to serve as the base class for testing discriminator support using elements.

## Structure

`BaseForDiscriminatorInElement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `discriminator` | `str` | Optional | The discriminator element. |
| `base_field` | `str` | Required | String element in parent model. |

## Example (as XML)

```xml
<discriminated>
  <discrim>Anakin Skywalker</discrim>
  <inherited>Base Field0</inherited>
</discriminated>
```

