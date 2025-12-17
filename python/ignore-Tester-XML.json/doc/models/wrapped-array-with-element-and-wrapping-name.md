
# Wrapped Array With Element and Wrapping Name

A model containing a string array

## Structure

`WrappedArrayWithElementAndWrappingName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `elem` | `List[str]` | Required | A string array that should be wrapped in another element.  The wrapping element's xml name should be "elements" and the xml names of the elements should be "animal" |

## Example (as XML)

```xml
<wrappedArrayWithElementAndWrappingName>
  <elements>
    <animal>elem7</animal>
    <animal>elem6</animal>
  </elements>
</wrappedArrayWithElementAndWrappingName>
```

