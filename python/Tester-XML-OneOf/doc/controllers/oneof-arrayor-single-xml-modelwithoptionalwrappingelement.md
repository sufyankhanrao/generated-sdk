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

[`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md)

## Example Usage

```python
result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate()
print(result)
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

`Any`

## Example Usage

```python
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate(body)
print(result)
```


# Generate 1

This endpoint returns a 'CatsOrADogOrWolves' model as xml.

```python
def generate_1(self)
```

## Response Type

[`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md)

## Example Usage

```python
result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate_1()
print(result)
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

`Any`

## Example Usage

```python
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate_1(body)
print(result)
```


# Generate 2

This endpoint returns a 'CatsOrADogOrWolves' model as xml.

```python
def generate_2(self)
```

## Response Type

[`CatsOrADogOrWolves`](../../doc/models/cats-or-a-dog-or-wolves.md)

## Example Usage

```python
result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.generate_2()
print(result)
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

`Any`

## Example Usage

```python
body = CatsOrADogOrWolves(
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = oneof_array_or_single_xml_model_with_optional_wrapping_element_controller.validate_2(body)
print(result)
```

