# User

```python
user_controller = client.user
```

## Class Name

`UserController`


# Get User

```python
def get_user(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserModel`](../../doc/models/user-model.md).

## Example Usage

```python
result = user_controller.get_user()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

