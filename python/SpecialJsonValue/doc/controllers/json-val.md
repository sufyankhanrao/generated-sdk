# Json Val

```python
json_val_controller = client.json_val
```

## Class Name

`JsonValController`

## Methods

* [Send Valuein Model](../../doc/controllers/json-val.md#send-valuein-model)
* [Send Valueas Body](../../doc/controllers/json-val.md#send-valueas-body)
* [Send Valueas Form](../../doc/controllers/json-val.md#send-valueas-form)
* [Send Valueas Query](../../doc/controllers/json-val.md#send-valueas-query)
* [Get Value](../../doc/controllers/json-val.md#get-value)
* [Get Value Array](../../doc/controllers/json-val.md#get-value-array)
* [Get Value Map](../../doc/controllers/json-val.md#get-value-map)
* [Get Valuein Model](../../doc/controllers/json-val.md#get-valuein-model)


# Send Valuein Model

Send Value in Model

```python
def send_valuein_model(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ValueContainer`](../../doc/models/value-container.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = ValueContainer(
    name='a name',
    id='definition-123',
    value=jsonpickle.decode('{"key1":"val1","key2":"val2"}')
)

result = json_val_controller.send_valuein_model(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Valueas Body

Send Value as Body

```python
def send_valueas_body(self,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `Any` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = jsonpickle.decode('{"key1":"val1","key2":"val2"}')

result = json_val_controller.send_valueas_body(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Valueas Form

Send Value as Form

```python
def send_valueas_form(self,
                     options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Header, Required | - |
| `id` | `int` | Form, Required | - |
| `model` | `Any` | Form, Required | - |
| `model_array` | `List[Any]` | Form, Optional | - |
| `model_map` | `Dict[str, Any]` | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'content_type': ContentType.ENUM_APPLICATIONXWWWFORMURLENCODED,
    'id': 112,
    'model': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
}
result = json_val_controller.send_valueas_form(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Valueas Query

Send Value as Query

```python
def send_valueas_query(self,
                      options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Query, Required | - |
| `model` | `Any` | Query, Required | - |
| `model_array` | `List[Any]` | Query, Optional | - |
| `model_map` | `Dict[str, Any]` | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'id': 112,
    'model': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
}
result = json_val_controller.send_valueas_query(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Value

Get Value

```python
def get_value(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
result = json_val_controller.get_value()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Value Array

Get Value Array

```python
def get_value_array(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[Any]`.

## Example Usage

```python
result = json_val_controller.get_value_array()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Value Map

Get Value Map

```python
def get_value_map(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Dict[str, Any]`.

## Example Usage

```python
result = json_val_controller.get_value_map()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Valuein Model

Get Value in Model

```python
def get_valuein_model(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ValueContainer`](../../doc/models/value-container.md).

## Example Usage

```python
result = json_val_controller.get_valuein_model()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

