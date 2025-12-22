# Files

```python
files_controller = client.files
```

## Class Name

`FilesController`


# Get File Count

```python
def get_file_count(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Response`](../../doc/models/response.md).

## Example Usage

```python
result = files_controller.get_file_count()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

