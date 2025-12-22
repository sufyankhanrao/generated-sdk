# Binary Params

```python
binary_params_controller = client.binary_params
```

## Class Name

`BinaryParamsController`

## Methods

* [Send File](../../doc/controllers/binary-params.md#send-file)
* [Send Image With Constant Content-Type](../../doc/controllers/binary-params.md#send-image-with-constant-content-type)
* [Send Image With Configured Content-Type](../../doc/controllers/binary-params.md#send-image-with-configured-content-type)


# Send File

```python
def send_file(self,
             file)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = binary_params_controller.send_file(file)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Image With Constant Content-Type

```python
def send_image_with_constant_content_type(self,
                                         image)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `image` | `typing.BinaryIO` | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
image = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = binary_params_controller.send_image_with_constant_content_type(image)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Image With Configured Content-Type

```python
def send_image_with_configured_content_type(self,
                                           options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | `str` | Header, Required | - |
| `image` | `typing.BinaryIO` | Body, Required | - |
| `is_image` | `str` | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'content_type': 'content-type8',
    'image': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'is_image': 'true'
}
result = binary_params_controller.send_image_with_configured_content_type(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

