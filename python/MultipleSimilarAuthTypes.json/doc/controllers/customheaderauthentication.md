# Customheaderauthentication

```python
customheaderauthentication_controller = client.customheaderauthentication
```

## Class Name

`CustomheaderauthenticationController`


# Get Test Custom Authentication

```python
def get_test_custom_authentication(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = custom_header_authentication_controller.get_test_custom_authentication()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

