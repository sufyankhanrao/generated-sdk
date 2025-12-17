
# Discriminator in Element

The child model to be used for testing discriminator support using elements.

## Structure

`DiscriminatorInElement`

## Inherits From

[`BaseForDiscriminatorInElement`](../../doc/models/base-for-discriminator-in-element.md)

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `added_field` | `str` | Required | String element in child model. |

## Example (as XML)

```xml
<discriminated>
  <discrim>Luke Skywalker</discrim>
  <inherited>Base Field0</inherited>
  <added>Added Field2</added>
</discriminated>
```

