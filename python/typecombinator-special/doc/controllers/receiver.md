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

List[[Days](../../doc/models/days-enum.md) | [MonthName](../../doc/models/month-name-enum.md) | [MonthNumber](../../doc/models/month-number-enum.md)]

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.enum_param(case)
print(result)
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

List[date | datetime]

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.date_time_param(case)
print(result)
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

[Cat](../../doc/models/cat.md) | [Dog](../../doc/models/dog.md) | [Rabbit](../../doc/models/rabbit.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.req_opt_param(case)
print(result)
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

[`MultipleEnums`](../../doc/models/multiple-enums.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.multiple_enums(case)
print(result)
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

[`DateTimeCases`](../../doc/models/date-time-cases.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.date_time_cases(case)
print(result)
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

[`FactoringSchema`](../../doc/models/factoring-schema.md)

## Example Usage

```python
case = CaseEnum.CASEA

result = receiver_controller.factoring_schema(case)
print(result)
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

[`OuterModel`](../../doc/models/outer-model.md)

## Example Usage

```python
result = receiver_controller.get_enum_in_nested_model()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | - | `APIException` |

