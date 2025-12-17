# Team Logins

```python
team_logins_controller = client.team_logins
```

## Class Name

`TeamLoginsController`

## Methods

* [Get Team Logins Id](../../doc/controllers/team-logins.md#get-team-logins-id)
* [Put Team Logins Id](../../doc/controllers/team-logins.md#put-team-logins-id)
* [Delete Team Logins Id](../../doc/controllers/team-logins.md#delete-team-logins-id)
* [Get Team Logins](../../doc/controllers/team-logins.md#get-team-logins)
* [Post Team Logins](../../doc/controllers/team-logins.md#post-team-logins)


# Get Team Logins Id

Query a teamLogins or Team Login resource that represents the link between a Login and a Team as well as the Login's rights on the Team, where the Login resource identified in its 'login' field is considered part of the Team.

```python
def get_team_logins_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this team login. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamLoginResponseResult`](../../doc/models/team-login-response-result.md).

## Example Usage

```python
id = 't1_tel_6802c54d22f16393d4be00z'

request_token = '20250423-yourmerchant-refunds-001'

result = team_logins_controller.get_team_logins_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_tel_6802c54d22f16393d4be00z",
        "created": "2025-04-18 17:34:05.1626",
        "modified": "2025-04-18 17:34:05.1626",
        "creator": "t1_log_67c4d37d494077b9db8faf0",
        "modifier": "t1_log_67c4d37d494077b9db8faf0",
        "login": "t1_log_6802c54cba888f6abfd88cc",
        "team": "t1_tem_6621af6c10f4a29427a2d35",
        "create": 0,
        "read": 0,
        "update": 0,
        "delete": 0,
        "reference": 0,
        "teamAdmin": 0
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Put Team Logins Id

Update a teamLogins or Team Login resource, representing the link between a Login and a Team as well as the Login's rights on the Team, where the Login resource identified in its 'login' field is considered part of the Team.

```python
def put_team_logins_id(self,
                      id,
                      body,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this team's login. |
| `body` | [`TeamLoginPutRequest`](../../doc/models/team-login-put-request.md) | Body, Required | Update Team Login Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamLoginResponseResult`](../../doc/models/team-login-response-result.md).

## Example Usage

```python
id = 't1_tel_6802c54d22f16393d4be00z'

body = TeamLoginPutRequest(
    login='t1_log_6802c54cba888f6abfd88cc',
    team='t1_tem_6621af6c10f4a29427a2d35',
    create=CreateEnum.ENUM_NONE,
    read=TeamLoginReadEnum.ENUM_NONE,
    update=UpdateEnum.ENUM_NONE,
    delete=DeleteEnum.ENUM_NONE,
    reference=ReferenceEnum.ENUM_NONE,
    team_admin=TeamAdminEnum.ENUM_NONE
)

request_token = '20250423-yourmerchant-refunds-001'

result = team_logins_controller.put_team_logins_id(
    id,
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_tel_6802c54d22f16393d4be00z",
        "created": "2025-04-18 17:34:05.1626",
        "modified": "2025-04-18 17:34:05.1626",
        "creator": "t1_log_67c4d37d494077b9db8faf0",
        "modifier": "t1_log_67c4d37d494077b9db8faf0",
        "login": "t1_log_6802c54cba888f6abfd88cc",
        "team": "t1_tem_6621af6c10f4a29427a2d35",
        "create": 0,
        "read": 0,
        "update": 0,
        "delete": 0,
        "reference": 0,
        "teamAdmin": 0
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Delete Team Logins Id

Delete a Team Login, which represents the link between a Login and a Team as well as the Login's rights on the Team, where the Login resource identified in its 'login' field is considered part of the Team.

```python
def delete_team_logins_id(self,
                         id,
                         request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this team login. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamLoginResponseResult`](../../doc/models/team-login-response-result.md).

## Example Usage

```python
id = 't1_tel_6802c54d22f16393d4be00z'

request_token = '20250423-yourmerchant-refunds-001'

result = team_logins_controller.delete_team_logins_id(
    id,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_tel_6802c54d22f16393d4be00z",
        "created": "2025-04-18 17:34:05.1626",
        "modified": "2025-04-18 17:34:05.1626",
        "creator": "t1_log_67c4d37d494077b9db8faf0",
        "modifier": "t1_log_67c4d37d494077b9db8faf0",
        "login": "t1_log_6802c54cba888f6abfd88cc",
        "team": "t1_tem_6621af6c10f4a29427a2d35",
        "create": 0,
        "read": 0,
        "update": 0,
        "delete": 0,
        "reference": 0,
        "teamAdmin": 0
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Get Team Logins

Query a teamLogins resource.
A teamLogins resource represents the link between a Login and a Team as well as the Login's rights on the Team. The Login resource identified in its 'login' field is considered part of the Team.

```python
def get_team_logins(self,
                   request_token=None,
                   search=None,
                   totals=None,
                   page_number=None,
                   page_limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |
| `totals` | `str` | Header, Optional | To configure a request to return a total for all instances of a field in a result set,  use the totals header in the format `totals={operator}[]={key}`.  This will calculate the desired total and return it in the `details > totals` object of the response.  For instance, if you want to sum the `total` field of all transactions,  you would use the `sum` operator. The response will include the result set,  along with the calculated total in the `details` section. See [Collection Operators](page:welcome#collection-operators) for detailed information and examples on how to use totals header. |
| `page_number` | `int` | Query, Optional | Set this path parameter to request a specific page of records.<br>For example, set `?page[number]=2` to retrieve the second page of records for this request. |
| `page_limit` | `int` | Query, Optional | Set this path parameter to request up to a specific amount of records. By default 30 records are retrieved per page. The maximum limit that can be set is 100.<br>For example, set `?page[limit]=50` to retrieve up to 50 records for this request. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamLoginResponseResult`](../../doc/models/team-login-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = team_logins_controller.get_team_logins(
    request_token=request_token,
    search=search,
    totals=totals,
    page_number=page_number,
    page_limit=page_limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_tel_6802c54d22f16393d4be00z",
        "created": "2025-04-18 17:34:05.1626",
        "modified": "2025-04-18 17:34:05.1626",
        "creator": "t1_log_67c4d37d494077b9db8faf0",
        "modifier": "t1_log_67c4d37d494077b9db8faf0",
        "login": "t1_log_6802c54cba888f6abfd88cc",
        "team": "t1_tem_6621af6c10f4a29427a2d35",
        "create": 0,
        "read": 0,
        "update": 0,
        "delete": 0,
        "reference": 0,
        "teamAdmin": 0
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |


# Post Team Logins

Create a teamLogins resource.
A teamLogins resource represents the link between a Login and a Team as well as the Login's rights on the Team. The Login resource identified in its 'login' field is considered part of the Team.

```python
def post_team_logins(self,
                    body,
                    request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TeamLoginPostRequest`](../../doc/models/team-login-post-request.md) | Body, Required | Create Team Login Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamLoginResponseResult`](../../doc/models/team-login-response-result.md).

## Example Usage

```python
body = TeamLoginPostRequest(
    login='t1_log_6802c54cba888f6abfd88cc',
    team='t1_tem_6621af6c10f4a29427a2d35',
    create=CreateEnum.ENUM_NONE,
    read=TeamLoginReadEnum.ENUM_NONE,
    update=UpdateEnum.ENUM_NONE,
    delete=DeleteEnum.ENUM_NONE,
    reference=ReferenceEnum.ENUM_NONE,
    team_admin=TeamAdminEnum.ENUM_NONE
)

request_token = '20250423-yourmerchant-refunds-001'

result = team_logins_controller.post_team_logins(
    body,
    request_token=request_token
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "response": {
    "data": [
      {
        "id": "t1_tel_6802c54d22f16393d4be00z",
        "created": "2025-04-18 17:34:05.1626",
        "modified": "2025-04-18 17:34:05.1626",
        "creator": "t1_log_67c4d37d494077b9db8faf0",
        "modifier": "t1_log_67c4d37d494077b9db8faf0",
        "login": "t1_log_6802c54cba888f6abfd88cc",
        "team": "t1_tem_6621af6c10f4a29427a2d35",
        "create": 0,
        "read": 0,
        "update": 0,
        "delete": 0,
        "reference": 0,
        "teamAdmin": 0
      }
    ],
    "details": {
      "requestId": "1",
      "totals": [],
      "page": {
        "current": 1,
        "last": 1,
        "hasMore": false
      }
    },
    "errors": []
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error | [`ErrorFourHundredException`](../../doc/models/error-four-hundred-exception.md) |

