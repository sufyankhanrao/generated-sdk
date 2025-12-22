# Form Params

```python
form_params_controller = client.form_params
```

## Class Name

`FormParamsController`

## Methods

* [Send Multiple Files](../../doc/controllers/form-params.md#send-multiple-files)
* [Send Collected Files](../../doc/controllers/form-params.md#send-collected-files)


# Send Multiple Files

```python
def send_multiple_files(self,
                       file,
                       file_1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |
| `file_1` | `typing.BinaryIO` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

file_1 = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = form_params_controller.send_multiple_files(
    file,
    file_1
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Send Collected Files

```python
def send_collected_files(self,
                        options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Form, Required | - |
| `file_1` | `typing.BinaryIO` | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
collect = {
    'file': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'file_1': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')
}
result = form_params_controller.send_collected_files(collect)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

