
# Scalar Model

This class contains scalar types in oneOf/anyOf cases.

## Structure

`ScalarModel`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `any_of_required` | float \| bool | Required | This is a container for any-of cases. |
| `one_of_req_nullable` | int \| str \| None | Required | This is a container for one-of cases. |
| `one_of_optional` | int \| float \| str \| None | Optional | This is a container for one-of cases. |
| `any_of_opt_nullable` | int \| bool \| None | Optional | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "anyOfRequired": 226.88,
  "oneOfReqNullable": 116,
  "oneOfOptional": 124,
  "anyOfOptNullable": 64
}
```

