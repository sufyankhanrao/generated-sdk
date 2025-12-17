# API

```python
client_controller = client.client
```

## Class Name

`APIController`


# Send User Agent

```python
def send_user_agent(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
result = client_controller.send_user_agent()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

