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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = SchemaContainer(
    name='a name',
    id='definition-123',
    schema={"key1":"val1","key2":"val2"}
)

result = json_obj_controller.send_schemain_model(body)
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = {"key1":"val1","key2":"val2"}

result = json_obj_controller.send_schemaas_body(body)
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'content_type': ContentType.ENUM_APPLICATIONXWWWFORMURLENCODED,
    'id': 112,
    'model': {"key1":"val1","key2":"val2"}
}
result = json_obj_controller.send_schemaas_form(collect)
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'id': 112,
    'model': {"key1":"val1","key2":"val2"}
}
result = json_obj_controller.send_schemaas_query(collect)
print(result)
```


# Get Schema

Get Schema

```python
def get_schema(self)
```

## Response Type

`dict`

## Example Usage

```python
result = json_obj_controller.get_schema()
print(result)
```


# Get Schema Array

Get Schema Array

```python
def get_schema_array(self)
```

## Response Type

`List[dict]`

## Example Usage

```python
result = json_obj_controller.get_schema_array()
print(result)
```


# Get Schema Map

Get Schema Map

```python
def get_schema_map(self)
```

## Response Type

`Dict[str, dict]`

## Example Usage

```python
result = json_obj_controller.get_schema_map()
print(result)
```


# Get Schemain Model

Get Schema in Model

```python
def get_schemain_model(self)
```

## Response Type

[`SchemaContainer`](../../doc/models/schema-container.md)

## Example Usage

```python
result = json_obj_controller.get_schemain_model()
print(result)
```

