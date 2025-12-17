
# Wrapped Array With Element Name

A model containing a string array

## Structure

`WrappedArrayWithElementName`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `elem` | `List[str]` | Required | A string array that should be wrapped in another element.  The wrapping element's xml name should be "elem" and the xml names of the elements should be "animal" |

## Example (as XML)

```xml
<wrappedArrayWithElementName>
  <elem>
    <animal>elem7</animal>
    <animal>elem8</animal>
    <animal>elem9</animal>
  </elem>
</wrappedArrayWithElementName>
```

