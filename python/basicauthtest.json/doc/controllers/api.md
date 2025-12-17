# API

```python
client_controller = client.client
```

## Class Name

`APIController`


# Get Basic Auth Test

```python
def get_basic_auth_test(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = client_controller.get_basic_auth_test()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

