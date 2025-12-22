# Json Obj

```python
json_obj_controller = client.json_obj
```

## Class Name

`JsonObjController`

## Methods

* [Send Schemain Model](../../doc/controllers/json-obj.md#send-schemain-model)
* [Send Schemaas Body](../../doc/controllers/json-obj.md#send-schemaas-body)
* [Send Schemaas Form](../../doc/controllers/json-obj.md#send-schemaas-form)
* [Send Schemaas Query](../../doc/controllers/json-obj.md#send-schemaas-query)
* [Get Schema](../../doc/controllers/json-obj.md#get-schema)
* [Get Schema Array](../../doc/controllers/json-obj.md#get-schema-array)
* [Get Schema Map](../../doc/controllers/json-obj.md#get-schema-map)
* [Get Schemain Model](../../doc/controllers/json-obj.md#get-schemain-model)


# Send Schemain Model

Send Schema in Model

```python
def send_schemain_model(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SchemaContainer`](../../doc/models/schema-container.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = SchemaContainer(
    name='a name',
    id='definition-123',
    schema={"key1":"val1","key2":"val2"}
)

result = json_obj_controller.send_schemain_model(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Schemaas Body

Send Schema as Body

```python
def send_schemaas_body(self,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `dict` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
body = {"key1":"val1","key2":"val2"}

result = json_obj_controller.send_schemaas_body(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Schemaas Form

Send Schema as Form

```python
def send_schemaas_form(self,
                      options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentType`](../../doc/models/content-type.md) | Header, Required | - |
| `id` | `int` | Form, Required | - |
| `model` | `dict` | Form, Required | - |
| `model_array` | `List[dict]` | Form, Optional | - |
| `model_map` | `Dict[str, dict]` | Form, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'content_type': ContentType.ENUM_APPLICATIONXWWWFORMURLENCODED,
    'id': 112,
    'model': {"key1":"val1","key2":"val2"}
}
result = json_obj_controller.send_schemaas_form(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Schemaas Query

Send Schema as Query

```python
def send_schemaas_query(self,
                       options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Query, Required | - |
| `model` | `dict` | Query, Required | - |
| `model_array` | `List[dict]` | Query, Optional | - |
| `model_map` | `Dict[str, dict]` | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'id': 112,
    'model': {"key1":"val1","key2":"val2"}
}
result = json_obj_controller.send_schemaas_query(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Schema

Get Schema

```python
def get_schema(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `dict`.

## Example Usage

```python
result = json_obj_controller.get_schema()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Schema Array

Get Schema Array

```python
def get_schema_array(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[dict]`.

## Example Usage

```python
result = json_obj_controller.get_schema_array()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Schema Map

Get Schema Map

```python
def get_schema_map(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Dict[str, dict]`.

## Example Usage

```python
result = json_obj_controller.get_schema_map()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Schemain Model

Get Schema in Model

```python
def get_schemain_model(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SchemaContainer`](../../doc/models/schema-container.md).

## Example Usage

```python
result = json_obj_controller.get_schemain_model()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

