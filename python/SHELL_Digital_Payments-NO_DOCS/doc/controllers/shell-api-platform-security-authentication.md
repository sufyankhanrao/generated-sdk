# Shell API Platform Security Authentication

```python
shell_api_platform_security_authentication_controller = client.shell_api_platform_security_authentication
```

## Class Name

`ShellAPIPlatformSecurityAuthenticationController`


# Oauth Token Post

To obtain APIGEE access token

:information_source: **Note** This endpoint does not require authentication.

```python
def oauth_token_post(self,
                    grant_type,
                    client_id,
                    client_secret)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_type` | `str` | Form, Required | In OAuth 2.0, the term grant typee refers to the way an application gets an access token. OAuth 2.0 defines several grant types, including the authorization code flow. |
| `client_id` | `str` | Form, Required | After registering your app, you will receive a client ID and a client secret. The client ID is considered public information, and is used to build login URLs, or included in Javascript source code on a page. |
| `client_secret` | `str` | Form, Required | After registering your app, you will receive a client ID and a client secret. The client ID is considered public information, and is used to build login URLs, or included in Javascript source code on a page. The client secret must be kept confidential. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AccessTokenResponse`](../../doc/models/access-token-response.md).

## Example Usage

```python
grant_type = 'client_credentials'

client_id = 'SOFflRakNlwnWlxfOXQ4GHDVyqGawuKA'

client_secret = 'cRnWgw7gACqM3gVS'

result = shell_api_platform_security_authentication_controller.oauth_token_post(
    grant_type,
    client_id,
    client_secret
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`AccessTokenErrorException`](../../doc/models/access-token-error-exception.md) |

