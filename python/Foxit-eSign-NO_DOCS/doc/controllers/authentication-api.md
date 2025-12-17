# Authentication API

```python
authentication_api_controller = client.authentication_api
```

## Class Name

`AuthenticationAPIController`


# Generate Access Token

Generate your Access Token

:information_source: **Note** This endpoint does not require authentication.

```python
def generate_access_token(self,
                         content_type,
                         client_id,
                         client_secret,
                         grant_type,
                         scope)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content_type` | [`ContentTypeEnum`](../../doc/models/content-type-enum.md) | Header, Required | - |
| `client_id` | `str` | Form, Required | - |
| `client_secret` | `str` | Form, Required | - |
| `grant_type` | [`GrantTypeEnum`](../../doc/models/grant-type-enum.md) | Form, Required | - |
| `scope` | [`ScopeEnum`](../../doc/models/scope-enum.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
content_type = ContentTypeEnum.ENUM_APPLICATIONXWWWFORMURLENCODED

client_id = 'client_id8'

client_secret = 'client_secret8'

grant_type = GrantTypeEnum.CLIENT_CREDENTIALS

scope = ScopeEnum.READWRITE

result = authentication_api_controller.generate_access_token(
    content_type,
    client_id,
    client_secret,
    grant_type,
    scope
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "access_token": "ACCESS_TOKEN",
  "token_type": "bearer",
  "expires_in": 31536000
}
```

