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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

file_1 = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = form_params_controller.send_multiple_files(
    file,
    file_1
)
print(result)
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

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
collect = {
    'file': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type'),
    'file_1': FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')
}
result = form_params_controller.send_collected_files(collect)
print(result)
```

