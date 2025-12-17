# User Token

```python
user_token_controller = client.user_token
```

## Class Name

`UserTokenController`

## Methods

* [Issue Token](../../doc/controllers/user-token.md#issue-token)
* [Renew Token](../../doc/controllers/user-token.md#renew-token)
* [Revoke Token](../../doc/controllers/user-token.md#revoke-token)


# Issue Token

When users interact with your Public API integration as staff members, they need to get a staff user token for authentication.
You can use the issue endpoint to get a staff user token, then pass the token in the headers for all of your requests.

:information_source: **Note** This endpoint does not require authentication.

```python
def issue_token(self,
               version,
               request,
               site_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`IssueRequest`](../../doc/models/issue-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IssueResponse`](../../doc/models/issue-response.md).

## Example Usage

```python
version = '6'

request = IssueRequest(
    username='Username4',
    password='Password6'
)

site_id = '-99'

result = user_token_controller.issue_token(
    version,
    request,
    site_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Renew Token

Renews a token. Can be used to extend the lifetime of a token.
Current lifetime expansion: 24hrs from current expiration, up to 7 renewals.

:information_source: **Note** This endpoint does not require authentication.

```python
def renew_token(self,
               version,
               site_id,
               authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = user_token_controller.renew_token(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Revoke Token

Revokes the user token in the Authorization header.

:information_source: **Note** This endpoint does not require authentication.

```python
def revoke_token(self,
                version,
                site_id,
                authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = user_token_controller.revoke_token(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

