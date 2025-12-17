# Entity Terms

```python
entity_terms_controller = client.entity_terms
```

## Class Name

`EntityTermsController`

## Methods

* [Get Entity Terms Id](../../doc/controllers/entity-terms.md#get-entity-terms-id)
* [Get Entity Terms](../../doc/controllers/entity-terms.md#get-entity-terms)
* [Post Entity Terms](../../doc/controllers/entity-terms.md#post-entity-terms)


# Get Entity Terms Id

Query an entityTerms.

```python
def get_entity_terms_id(self,
                       id,
                       request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityTermsResponseResult`](../../doc/models/entity-terms-response-result.md).

## Example Usage

```python
id = 't1_ett_6866623edadbe8685525ae1'

request_token = '20250423-yourmerchant-refunds-001'

result = entity_terms_controller.get_entity_terms_id(
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
        "id": "t1_ett_6866623edadbe8685525ae1",
        "created": "2025-07-03 06:58:06.9131",
        "creator": "g1577139c2304b7",
        "modified": "2025-07-03 06:58:06.9131",
        "modifier": "g1577139c2304b7",
        "entity": "t1_ent_6866623b54057c4c7590600",
        "type": "Payrix Submerchant Agreement",
        "version": "1.0",
        "versionId": "",
        "ip": "35.153.101.155",
        "dateAccepted": "2025-07-03 06:58:06",
        "inactive": 0,
        "frozen": 0
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


# Get Entity Terms

Query an entityTerms

```python
def get_entity_terms(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityTermsResponseResult`](../../doc/models/entity-terms-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = entity_terms_controller.get_entity_terms(
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
        "id": "t1_ett_6866623edadbe8685525ae1",
        "created": "2025-07-03 06:58:06.9131",
        "creator": "g1577139c2304b7",
        "modified": "2025-07-03 06:58:06.9131",
        "modifier": "g1577139c2304b7",
        "entity": "t1_ent_6866623b54057c4c7590600",
        "type": "Payrix Submerchant Agreement",
        "version": "1.0",
        "versionId": "",
        "ip": "35.153.101.155",
        "dateAccepted": "2025-07-03 06:58:06",
        "inactive": 0,
        "frozen": 0
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


# Post Entity Terms

Create an entityTerms.

```python
def post_entity_terms(self,
                     body,
                     request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`EntityTermsPostRequest`](../../doc/models/entity-terms-post-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityTermsResponseResult`](../../doc/models/entity-terms-response-result.md).

## Example Usage

```python
body = EntityTermsPostRequest(
    entity='t1_ett_6866623edadbe8685525ae1',
    mtype='Payrix Submerchant Agreement',
    version='1.0',
    version_id='',
    ip='35.153.101.155',
    date_accepted='2025-07-03 06:58:06',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = entity_terms_controller.post_entity_terms(
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
        "id": "t1_ett_6866623edadbe8685525ae1",
        "created": "2025-07-03 06:58:06.9131",
        "creator": "g1577139c2304b7",
        "modified": "2025-07-03 06:58:06.9131",
        "modifier": "g1577139c2304b7",
        "entity": "t1_ent_6866623b54057c4c7590600",
        "type": "Payrix Submerchant Agreement",
        "version": "1.0",
        "versionId": "",
        "ip": "35.153.101.155",
        "dateAccepted": "2025-07-03 06:58:06",
        "inactive": 0,
        "frozen": 0
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

