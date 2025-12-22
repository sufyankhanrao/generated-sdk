# Echo

```python
echo_controller = client.echo
```

## Class Name

`EchoController`

## Methods

* [Json Echo](../../doc/controllers/echo.md#json-echo)
* [Form Echo](../../doc/controllers/echo.md#form-echo)
* [Query Echo](../../doc/controllers/echo.md#query-echo)


# Json Echo

Echo's back the request

```python
def json_echo(self,
             input)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `input` | `Any` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
input = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = echo_controller.json_echo(input)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Form Echo

Sends the request including any form params as JSON

```python
def form_echo(self,
             input)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `input` | `Any` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
input = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = echo_controller.form_echo(input)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Query Echo

```python
def query_echo(self,
              _optional_query_parameters=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `_optional_query_parameters` | `array` | Optional | Pass additional query parameters. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EchoResponse`](../../doc/models/echo-response.md).

## Example Usage

```python
_optional_query_parameters = {
    'key0': 'additionalQueryParams2'
}

result = echo_controller.query_echo(
    _optional_query_parameters=_optional_query_parameters
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

