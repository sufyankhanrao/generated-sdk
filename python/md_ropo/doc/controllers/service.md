# Service

```python
service_controller = client.service
```

## Class Name

`ServiceController`


# Get Status

```python
def get_status(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServiceStatus`](../../doc/models/service-status.md).

## Example Usage

```python
result = service_controller.get_status()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

