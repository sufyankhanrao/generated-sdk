# Receiver

```python
receiver_controller = client.receiver
```

## Class Name

`ReceiverController`

## Methods

* [Scalar Param](../../doc/controllers/receiver.md#scalar-param)
* [Non Scalar Param](../../doc/controllers/receiver.md#non-scalar-param)
* [Mixed Param](../../doc/controllers/receiver.md#mixed-param)
* [Scalar Model](../../doc/controllers/receiver.md#scalar-model)
* [Non Scalar Model](../../doc/controllers/receiver.md#non-scalar-model)
* [Mixed Model](../../doc/controllers/receiver.md#mixed-model)


# Scalar Param

```python
def scalar_param(self,
                case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

List[float] | str

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.scalar_param(case)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Non Scalar Param

```python
def non_scalar_param(self,
                    case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

Dict[str, [Car](../../doc/models/car.md) | [Morning](../../doc/models/morning.md)]

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.non_scalar_param(case)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Mixed Param

```python
def mixed_param(self,
               case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

Dict[str, int] | Dict[str, [Atom](../../doc/models/atom.md)] | None

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.mixed_param(case)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Scalar Model

```python
def scalar_model(self,
                case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

[`ScalarModel`](../../doc/models/scalar-model.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.scalar_model(case)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Non Scalar Model

```python
def non_scalar_model(self,
                    case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

[`NonScalarModel`](../../doc/models/non-scalar-model.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.non_scalar_model(case)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Mixed Model

```python
def mixed_model(self,
               case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

[`MixedModel`](../../doc/models/mixed-model.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.mixed_model(case)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

