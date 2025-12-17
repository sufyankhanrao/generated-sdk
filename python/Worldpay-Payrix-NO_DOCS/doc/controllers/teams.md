# Teams

A team is an arbitrary grouping of user records that may have access provisioned on each other and can be attached to other resources as a unit for shared functionality.

```python
teams_controller = client.teams
```

## Class Name

`TeamsController`

## Methods

* [Get Teams Id](../../doc/controllers/teams.md#get-teams-id)
* [Put Teams Id](../../doc/controllers/teams.md#put-teams-id)
* [Delete Teams Id](../../doc/controllers/teams.md#delete-teams-id)
* [Get Teams](../../doc/controllers/teams.md#get-teams)
* [Post Teams](../../doc/controllers/teams.md#post-teams)


# Get Teams Id

Query a Team, which is a collection of Logins that you can associate by creating teamLogin resources.

```python
def get_teams_id(self,
                id,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this team. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamsResponseResult`](../../doc/models/teams-response-result.md).

## Example Usage

```python
id = 't1_tem_680155b5a6467e4911aa0z0'

request_token = '20250423-yourmerchant-refunds-001'

result = teams_controller.get_teams_id(
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
        "id": "t1_tem_680155b5a6467e4911aa0z0",
        "created": "2025-04-17 15:25:41.6956",
        "modified": "2025-04-17 15:25:41.6956",
        "creator": "t1_log_5deeafd8b9b491e28296a51",
        "modifier": "t1_log_5deeafd8b9b491e28296a51",
        "login": "t1_log_6801559c6218199cb0820df",
        "name": "merchant-team-t1_mer_680155985dbaab55256ecb0",
        "description": "Esmeralda McCullough Team",
        "autoCascadeDisabled": 0,
        "inactive": 0,
        "frozen": 0,
        "autoCascadeOwner": 0
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


# Put Teams Id

Update a Team, A Team is a collection of Logins, You can associate Logins with a Team by creating teamLogin resources.

```python
def put_teams_id(self,
                id,
                body,
                request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this team. |
| `body` | [`TeamsPutRequest`](../../doc/models/teams-put-request.md) | Body, Required | Update Team Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamsResponseResult`](../../doc/models/teams-response-result.md).

## Example Usage

```python
id = 't1_tem_680155b5a6467e4911aa0z0'

body = TeamsPutRequest(
    login='t1_log_6801559c6218199cb0820df',
    name='merchant-team-t1_mer_680155985dbaab55256ecb0',
    description='Esmeralda McCullough Team',
    auto_cascade_disabled=AutoCascadeDisabledEnum.DISABLED,
    auto_cascade_owner=AutoCascadeOwnerEnum.OFF,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = teams_controller.put_teams_id(
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
        "id": "t1_tem_680155b5a6467e4911aa0z0",
        "created": "2025-04-17 15:25:41.6956",
        "modified": "2025-04-17 15:25:41.6956",
        "creator": "t1_log_5deeafd8b9b491e28296a51",
        "modifier": "t1_log_5deeafd8b9b491e28296a51",
        "login": "t1_log_6801559c6218199cb0820df",
        "name": "merchant-team-t1_mer_680155985dbaab55256ecb0",
        "description": "Esmeralda McCullough Team",
        "autoCascadeDisabled": 0,
        "inactive": 0,
        "frozen": 0,
        "autoCascadeOwner": 0
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


# Delete Teams Id

Delete a Team, A Team is a collection of Logins, You can associate Logins with a Team by creating teamLogin resources.

```python
def delete_teams_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this team. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamsResponseResult`](../../doc/models/teams-response-result.md).

## Example Usage

```python
id = 't1_tem_680155b5a6467e4911aa0z0'

request_token = '20250423-yourmerchant-refunds-001'

result = teams_controller.delete_teams_id(
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
        "id": "t1_tem_680155b5a6467e4911aa0z0",
        "created": "2025-04-17 15:25:41.6956",
        "modified": "2025-04-17 15:25:41.6956",
        "creator": "t1_log_5deeafd8b9b491e28296a51",
        "modifier": "t1_log_5deeafd8b9b491e28296a51",
        "login": "t1_log_6801559c6218199cb0820df",
        "name": "merchant-team-t1_mer_680155985dbaab55256ecb0",
        "description": "Esmeralda McCullough Team",
        "autoCascadeDisabled": 0,
        "inactive": 0,
        "frozen": 0,
        "autoCascadeOwner": 0
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


# Get Teams

Query a Team.
A Team is a collection of Logins.
You can associate Logins with a Team by creating teamLogin resources.

```python
def get_teams(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamsResponseResult`](../../doc/models/teams-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = teams_controller.get_teams(
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
        "id": "t1_tem_680155b5a6467e4911aa0z0",
        "created": "2025-04-17 15:25:41.6956",
        "modified": "2025-04-17 15:25:41.6956",
        "creator": "t1_log_5deeafd8b9b491e28296a51",
        "modifier": "t1_log_5deeafd8b9b491e28296a51",
        "login": "t1_log_6801559c6218199cb0820df",
        "name": "merchant-team-t1_mer_680155985dbaab55256ecb0",
        "description": "Esmeralda McCullough Team",
        "autoCascadeDisabled": 0,
        "inactive": 0,
        "frozen": 0,
        "autoCascadeOwner": 0
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


# Post Teams

Create a Team.
A Team is a collection of Logins.
You can associate Logins with a Team by creating teamLogin resources.

```python
def post_teams(self,
              body,
              request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TeamsPostRequest`](../../doc/models/teams-post-request.md) | Body, Required | Create Team Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TeamsResponseResult`](../../doc/models/teams-response-result.md).

## Example Usage

```python
body = TeamsPostRequest(
    login='t1_log_6801559c6218199cb0820df',
    auto_cascade_disabled=AutoCascadeDisabledEnum.DISABLED,
    auto_cascade_owner=AutoCascadeOwnerEnum.OFF,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    name='merchant-team-t1_mer_680155985dbaab55256ecb0',
    description='Esmeralda McCullough Team'
)

request_token = '20250423-yourmerchant-refunds-001'

result = teams_controller.post_teams(
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
        "id": "t1_tem_680155b5a6467e4911aa0z0",
        "created": "2025-04-17 15:25:41.6956",
        "modified": "2025-04-17 15:25:41.6956",
        "creator": "t1_log_5deeafd8b9b491e28296a51",
        "modifier": "t1_log_5deeafd8b9b491e28296a51",
        "login": "t1_log_6801559c6218199cb0820df",
        "name": "merchant-team-t1_mer_680155985dbaab55256ecb0",
        "description": "Esmeralda McCullough Team",
        "autoCascadeDisabled": 0,
        "inactive": 0,
        "frozen": 0,
        "autoCascadeOwner": 0
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

