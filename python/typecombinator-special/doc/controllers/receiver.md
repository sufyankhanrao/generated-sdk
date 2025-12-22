# Receiver

```python
receiver_controller = client.receiver
```

## Class Name

`ReceiverController`

## Methods

* [Enum Param](../../doc/controllers/receiver.md#enum-param)
* [Date Time Param](../../doc/controllers/receiver.md#date-time-param)
* [Req Opt Param](../../doc/controllers/receiver.md#req-opt-param)
* [Multiple Enums](../../doc/controllers/receiver.md#multiple-enums)
* [Date Time Cases](../../doc/controllers/receiver.md#date-time-cases)
* [Factoring Schema](../../doc/controllers/receiver.md#factoring-schema)
* [Get Enum in Nested Model](../../doc/controllers/receiver.md#get-enum-in-nested-model)


# Enum Param

```python
def enum_param(self,
              case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[DaysEnum | MonthNameEnum | MonthNumberEnum]`.

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.enum_param(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Date Time Param

```python
def date_time_param(self,
                   case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[date | datetime]`.

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.date_time_param(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Req Opt Param

```python
def req_opt_param(self,
                 case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Cat | Dog | Rabbit`.

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.req_opt_param(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Multiple Enums

```python
def multiple_enums(self,
                  case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MultipleEnums`](../../doc/models/multiple-enums.md).

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.multiple_enums(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Date Time Cases

```python
def date_time_cases(self,
                   case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DateTimeCases`](../../doc/models/date-time-cases.md).

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.date_time_cases(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Factoring Schema

```python
def factoring_schema(self,
                    case)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | [`CaseEnum`](../../doc/models/case-enum.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FactoringSchema`](../../doc/models/factoring-schema.md).

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.factoring_schema(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |


# Get Enum in Nested Model

```python
def get_enum_in_nested_model(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OuterModel`](../../doc/models/outer-model.md).

## Example Usage

```python
result = receiver_controller.get_enum_in_nested_model()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

