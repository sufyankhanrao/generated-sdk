# Entity Refs

An entityRef may be used to store referential IDs for merchants,  facilitators and even vendors. For a merchant, at least a mid and funding entityRef is required for proper transacting and funding.  For a facilitator, at least the entity and funding entityRefs should be defined for proper merchant boarding,  transaction processing and funding operations as well as any other references required for operating on the selected platform.

```python
entity_refs_controller = client.entity_refs
```

## Class Name

`EntityRefsController`

## Methods

* [Get Entity Refs Id](../../doc/controllers/entity-refs.md#get-entity-refs-id)
* [Get Entity Refs](../../doc/controllers/entity-refs.md#get-entity-refs)


# Get Entity Refs Id

Query an EntityRefs resource that represents a reference code issued by the Processor that represents a particular Entity.

```python
def get_entity_refs_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this entity reference. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityRefsResponseResult`](../../doc/models/entity-refs-response-result.md).

## Example Usage

```python
id = 't1_erf_67c6cec3bae7182e38d05b0'

request_token = '20250423-yourmerchant-refunds-001'

result = entity_refs_controller.get_entity_refs_id(
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
        "id": "t1_erf_67c6cec3bae7182e38d05b0",
        "created": "2025-03-04 04:58:27.7684",
        "modified": "2025-03-04 04:58:27.7684",
        "creator": "t1_log_5e2888af4800e540557ece0",
        "modifier": "t1_log_5e2888af4800e540557ece0",
        "entity": "t1_ent_67c6ceba8a94b8cea9664f3",
        "ref": "7c6cec3badbf",
        "stage": "create",
        "platform": "VCORE",
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "member": "",
        "default": 0,
        "fundingCurrency": "USD",
        "options": "",
        "entityRoute": "g1599c89ae26f9c",
        "staging": 0,
        "fbo": ""
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


# Get Entity Refs

Query an EntityRefs resource that represents a reference code issued by the Processor that represents a particular Entity.

```python
def get_entity_refs(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityRefsResponseResult`](../../doc/models/entity-refs-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = entity_refs_controller.get_entity_refs(
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
        "id": "t1_erf_67c6cec3bae7182e38d05b0",
        "created": "2025-03-04 04:58:27.7684",
        "modified": "2025-03-04 04:58:27.7684",
        "creator": "t1_log_5e2888af4800e540557ece0",
        "modifier": "t1_log_5e2888af4800e540557ece0",
        "entity": "t1_ent_67c6ceba8a94b8cea9664f3",
        "ref": "7c6cec3badbf",
        "stage": "create",
        "platform": "VCORE",
        "currency": "USD",
        "inactive": 0,
        "frozen": 0,
        "member": "",
        "default": 0,
        "fundingCurrency": "USD",
        "options": "",
        "entityRoute": "g1599c89ae26f9c",
        "staging": 0,
        "fbo": ""
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

