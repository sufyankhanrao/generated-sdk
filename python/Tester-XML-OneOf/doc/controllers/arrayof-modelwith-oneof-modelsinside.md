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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ArrayOfCatOrDogObjects`](../../doc/models/array-of-cat-or-dog-objects.md).

## Example Usage

```python
result = array_of_model_with_oneof_models_inside_controller.generate()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

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

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Generate 1

This endpoint returns a 'ArrayOfCatOrDogObjects' model as xml.

```python
def generate_1(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ArrayOfCatOrDogObjects`](../../doc/models/array-of-cat-or-dog-objects.md).

## Example Usage

```python
result = array_of_model_with_oneof_models_inside_controller.generate_1()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

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

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

