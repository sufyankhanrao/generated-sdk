# Simple Calculator

```python
simple_calculator_controller = client.simple_calculator
```

## Class Name

`SimpleCalculatorController`


# Get Calculate

Calculates the expression using the specified operation.

```python
def get_calculate(self,
                 options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `operation` | [`OperationTypeEnum`](../../doc/models/operation-type-enum.md) | Template, Required | The operator to apply on the variables. [Example link](../../doc/models/operation-type-enum.md) |
| `x` | `float` | Query, Required | The LHS value |
| `y` | `float` | Query, Required | The RHS value |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `float`.

## Example Usage

```python
collect = {
    'operation': OperationTypeEnum.MULTIPLY,
    'x': 222.14,
    'y': 165.14
}
result = simple_calculator_controller.get_calculate(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

