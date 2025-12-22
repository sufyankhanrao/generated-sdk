# API

```python
client_controller = client.client
```

## Class Name

`APIController`


# Get O Auth 2 Test

Testing OAuth2.

```python
def get_o_auth_2_test(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = client_controller.get_o_auth_2_test()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

