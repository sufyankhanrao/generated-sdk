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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[Dict[str, int | bool | str]] | None`.

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.scalar_param(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Dict[str, List[Atom] | Atom]`.

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.non_scalar_param(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[Dict[str, bool]] | List[Dict[str, Vehicle]]`.

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.mixed_param(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ScalarModel`](../../doc/models/scalar-model.md).

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.scalar_model(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NonScalarModel`](../../doc/models/non-scalar-model.md).

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.non_scalar_model(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MixedModel`](../../doc/models/mixed-model.md).

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.mixed_model(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

