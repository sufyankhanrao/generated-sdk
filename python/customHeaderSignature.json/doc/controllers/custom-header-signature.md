# Custom Header Signature

```python
custom_header_signature_controller = client.custom_header_signature
```

## Class Name

`CustomHeaderSignatureController`


# Get Custom Header Signature

```python
def get_custom_header_signature(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = custom_header_signature_controller.get_custom_header_signature()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

