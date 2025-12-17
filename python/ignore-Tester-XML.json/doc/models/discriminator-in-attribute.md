
# Discriminator in Attribute

The child model to be used for testing discriminator support using attributes.

## Structure

`DiscriminatorInAttribute`

## Inherits From

[`BaseForDiscriminatorInAttribute`](../../doc/models/base-for-discriminator-in-attribute.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added_field` | `str` | Required | String element in child model. |

## Example (as XML)

```xml
<discriminated discrim="Kylo Ren">
  <inherited>Base Field8</inherited>
  <added>Added Field6</added>
</discriminated>
```

