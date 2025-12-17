
# Scalar Model

This class contains scalar types in oneOf/anyOf cases.

## Structure

`ScalarModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `single_inner_map` | Dict[str, float] \| bool | Required | This is a container for any-of cases. |
| `all_inner_array` | List[int] \| List[str] \| None | Required | This is a container for one-of cases. |
| `outer_array` | List[int \| float \| str] \| None | Optional | This is List of a container for one-of cases. |
| `outer_map` | Dict[str, int \| bool] \| None | Optional | This is Dictionary of a container for any-of cases. |
| `inner_nullable` | int \| None \| Any | Optional | This is a container for any-of cases. |
| `inner_array_with_nullable` | List[int] \| List[Any] \| None | Optional | This is a container for any-of cases. |
| `inner_map_with_nullable` | Dict[str, int] \| Dict[str, Any] \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "singleInnerMap": {
    "key0": 31.02,
    "key1": 31.03
  },
  "allInnerArray": [
    212,
    213,
    214
  ],
  "outerArray": [
    108,
    107
  ],
  "outerMap": {
    "key0": 13,
    "key1": 14,
    "key2": 15
  },
  "innerNullable": 120,
  "innerArrayWithNullable": [
    252
  ],
  "innerMapWithNullable": {
    "key0": 36
  }
}
```

