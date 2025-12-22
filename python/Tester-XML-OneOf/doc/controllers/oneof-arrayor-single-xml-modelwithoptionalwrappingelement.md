# Oneof Arrayor Single Xml Modelwithoptionalwrappingelement

```python
oneof_arrayor_single_xml_modelwithoptionalwrappingelement_controller = client.oneof_arrayor_single_xml_modelwithoptionalwrappingelement
```

## Class Name

`OneofArrayorSingleXmlModelwithoptionalwrappingelementController`

## Methods

* [Generate](../../doc/controllers/oneof-arrayor-single-xml-modelwithoptionalwrappingelement.md#generate)
* [Validate](../../doc/controllers/oneof-arrayor-single-xml-modelwithoptionalwrappingelement.md#validate)
* [Generate 1](../../doc/controllers/oneof-arrayor-single-xml-modelwithoptionalwrappingelement.md#generate-1)
* [Validate 1](../../doc/controllers/oneof-arrayor-single-xml-modelwithoptionalwrappingelement.md#validate-1)
* [Generate 2](../../doc/controllers/oneof-arrayor-single-xml-modelwithoptionalwrappingelement.md#generate-2)
* [Validate 2](../../doc/controllers/oneof-arrayor-single-xml-modelwithoptionalwrappingelement.md#validate-2)


# Generate

This endpoint returns a 'CatsOrADogOrWolves' model as xml.

```python
def generate(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md).

## Example Usage

```python
result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate

This endpoint expects a 'CatsOrADogOrWolves' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Generate 1

This endpoint returns a 'CatsOrADogOrWolves' model as xml.

```python
def generate_1(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md).

## Example Usage

```python
result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate_1()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate 1

This endpoint expects a 'CatsOrADogOrWolves' model as xml.

```python
def validate_1(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate_1(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Generate 2

This endpoint returns a 'CatsOrADogOrWolves' model as xml.

```python
def generate_2(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md).

## Example Usage

```python
result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate_2()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Validate 2

This endpoint expects a 'CatsOrADogOrWolves' model as xml.

```python
def validate_2(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate_2(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

