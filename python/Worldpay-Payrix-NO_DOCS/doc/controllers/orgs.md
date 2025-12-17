# Orgs

Resource that deals with records of all orgs. An org is an arbitrary grouping of entity records that can be attached to other resources as a unit for shared functionality.

```python
orgs_controller = client.orgs
```

## Class Name

`OrgsController`

## Methods

* [Get Orgs Id](../../doc/controllers/orgs.md#get-orgs-id)
* [Put Orgs Id](../../doc/controllers/orgs.md#put-orgs-id)
* [Delete Orgs Id](../../doc/controllers/orgs.md#delete-orgs-id)
* [Get Orgs](../../doc/controllers/orgs.md#get-orgs)
* [Post Orgs](../../doc/controllers/orgs.md#post-orgs)


# Get Orgs Id

Query an Org, which is a collection of Entities that you can associate with by creating orgEntity resources.

```python
def get_orgs_id(self,
               id,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and the Org ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsResponseResult`](../../doc/models/orgs-response-result.md).

## Example Usage

```python
id = 't1_org_67cab1c56e1fd4f4c0a355z'

request_token = '20250423-yourmerchant-refunds-001'

result = orgs_controller.get_orgs_id(
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
        "id": "t1_org_67cab1c56e1fd4f4c0a000z",
        "created": "2025-03-07 03:43:49.4586",
        "modified": "2025-03-07 03:43:49.4586",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "login": "t1_log_656d51cd565edf13a27c494",
        "name": "Leora44",
        "description": "description of Org",
        "defaultFeeFromEntity": ""
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


# Put Orgs Id

Update an Org, which is a collection of Entities that you can associate with other entities by creating orgEntity resources.

```python
def put_orgs_id(self,
               id,
               body,
               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and the Org ID. |
| `body` | [`OrgsPutRequest`](../../doc/models/orgs-put-request.md) | Body, Required | Update an Org Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsResponseResult`](../../doc/models/orgs-response-result.md).

## Example Usage

```python
id = 't1_org_67cab1c56e1fd4f4c0a355z'

body = OrgsPutRequest(
    login='t1_log_656d51cd565edf13a27c494',
    name='Leora44',
    description='description of Org'
)

request_token = '20250423-yourmerchant-refunds-001'

result = orgs_controller.put_orgs_id(
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
        "id": "t1_org_67cab1c56e1fd4f4c0a000z",
        "created": "2025-03-07 03:43:49.4586",
        "modified": "2025-03-07 03:43:49.4586",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "login": "t1_log_656d51cd565edf13a27c494",
        "name": "Leora44",
        "description": "description of Org",
        "defaultFeeFromEntity": ""
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


# Delete Orgs Id

Delete an Organization, which is a collection of Entities that you can associate with it by creating organization-entity resources.

```python
def delete_orgs_id(self,
                  id,
                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource and The Org ID. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsResponseResult`](../../doc/models/orgs-response-result.md).

## Example Usage

```python
id = 't1_org_67cab1c56e1fd4f4c0a355z'

request_token = '20250423-yourmerchant-refunds-001'

result = orgs_controller.delete_orgs_id(
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
        "id": "t1_org_67cab1c56e1fd4f4c0a000z",
        "created": "2025-03-07 03:43:49.4586",
        "modified": "2025-03-07 03:43:49.4586",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "login": "t1_log_656d51cd565edf13a27c494",
        "name": "Leora44",
        "description": "description of Org",
        "defaultFeeFromEntity": ""
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


# Get Orgs

Query an Org, which is a collection of Entities, To associate Entities with an Org use the [orgEntity](../../doc/controllers/org-entities.md#get-org-entities-id) endpoint. You will need the created Org ID when adding entities, such as a Merchant, to the Organization.

```python
def get_orgs(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsResponseResult`](../../doc/models/orgs-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = orgs_controller.get_orgs(
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
        "id": "t1_org_67cab1c56e1fd4f4c0a000z",
        "created": "2025-03-07 03:43:49.4586",
        "modified": "2025-03-07 03:43:49.4586",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "login": "t1_log_656d51cd565edf13a27c494",
        "name": "Leora44",
        "description": "description of Org",
        "defaultFeeFromEntity": ""
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


# Post Orgs

Create an Org which is a collection of Entities, To associate Entities with an Org use the [orgEntity](../../doc/controllers/org-entities.md#get-org-entities-id) endpoint. You will need the created Org ID when adding entities, such as a Merchant, to the Organization.

```python
def post_orgs(self,
             body,
             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OrgsPostRequest`](../../doc/models/orgs-post-request.md) | Body, Required | Create Org Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OrgsResponseResult`](../../doc/models/orgs-response-result.md).

## Example Usage

```python
body = OrgsPostRequest(
    login='t1_log_656d51cd565edf13a27c494',
    name='Leora44',
    description='description of Org'
)

request_token = '20250423-yourmerchant-refunds-001'

result = orgs_controller.post_orgs(
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
        "id": "t1_org_67cab1c56e1fd4f4c0a000z",
        "created": "2025-03-07 03:43:49.4586",
        "modified": "2025-03-07 03:43:49.4586",
        "creator": "t1_log_656d51cd565edf13a27c494",
        "modifier": "t1_log_656d51cd565edf13a27c494",
        "login": "t1_log_656d51cd565edf13a27c494",
        "name": "Leora44",
        "description": "description of Org",
        "defaultFeeFromEntity": ""
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

