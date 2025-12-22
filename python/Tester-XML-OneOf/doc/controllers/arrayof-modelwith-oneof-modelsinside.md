# Arrayof Modelwith Oneof Modelsinside

```python
arrayof_modelwith_oneof_modelsinside_controller = client.arrayof_modelwith_oneof_modelsinside
```

## Class Name

`ArrayofModelwithOneofModelsinsideController`

## Methods

* [Generate](../../doc/controllers/arrayof-modelwith-oneof-modelsinside.md#generate)
* [Validate](../../doc/controllers/arrayof-modelwith-oneof-modelsinside.md#validate)
* [Generate 1](../../doc/controllers/arrayof-modelwith-oneof-modelsinside.md#generate-1)
* [Validate 1](../../doc/controllers/arrayof-modelwith-oneof-modelsinside.md#validate-1)


# Generate

This endpoint returns a 'ArrayOfCatOrDogObjects' model as xml.

```python
def generate(self)
```

## Response Type

[`ArrayOfCatOrDogObjects`](../../doc/models/array-of-cat-or-dog-objects.md)

## Example Usage

```python
result = array_of_model_with_oneof_models_inside_controller.generate()
print(result)
```


# Validate

This endpoint expects a 'ArrayOfCatOrDogObjects' model as xml.

```python
def validate(self,
            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ArrayOfCatOrDogObjects`](../../doc/models/array-of-cat-or-dog-objects.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = ArrayOfCatOrDogObjects(
    value=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)

result = array_of_model_with_oneof_models_inside_controller.validate(body)
print(result)
```


# Generate 1

This endpoint returns a 'ArrayOfCatOrDogObjects' model as xml.

```python
def generate_1(self)
```

## Response Type

[`ArrayOfCatOrDogObjects`](../../doc/models/array-of-cat-or-dog-objects.md)

## Example Usage

```python
result = array_of_model_with_oneof_models_inside_controller.generate_1()
print(result)
```


# Validate 1

This endpoint expects a 'ArrayOfCatOrDogObjects' model as xml.

```python
def validate_1(self,
              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ArrayOfCatOrDogObjects`](../../doc/models/array-of-cat-or-dog-objects.md) | Body, Required | - |

## Response Type

`Any`

## Example Usage

```python
body = ArrayOfCatOrDogObjects(
    value=[
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    ]
)

result = array_of_model_with_oneof_models_inside_controller.validate_1(body)
print(result)
```

