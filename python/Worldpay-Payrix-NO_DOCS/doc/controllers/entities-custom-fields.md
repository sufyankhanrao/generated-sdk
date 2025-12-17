# Entities Custom Fields

the Entity Custom Fields feature, designed to empower partners to send identifiers and Risk-requested items using unlimited custom fields.  By leveraging this feature, partners can ensure that their software works seamlessly, leading to increased Boarding Rates. Additionally,  partners can avoid waiting for Risk to request information manually, streamlining their operations.

```python
entities_custom_fields_controller = client.entities_custom_fields
```

## Class Name

`EntitiesCustomFieldsController`

## Methods

* [Get Entity Custom Fields Id](../../doc/controllers/entities-custom-fields.md#get-entity-custom-fields-id)
* [Put Entity Custom Fields Id](../../doc/controllers/entities-custom-fields.md#put-entity-custom-fields-id)
* [Delete Entity Custom Fields Id](../../doc/controllers/entities-custom-fields.md#delete-entity-custom-fields-id)
* [Get Entity Custom Fields](../../doc/controllers/entities-custom-fields.md#get-entity-custom-fields)
* [Post Entity Custom Fields](../../doc/controllers/entities-custom-fields.md#post-entity-custom-fields)


# Get Entity Custom Fields Id

Query an Entity Custom Field.
Custom Fields can be added to entities associated by the Entity Id.
An Entity Id can have various fields associated to it.

```python
def get_entity_custom_fields_id(self,
                               id,
                               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityCustomFieldsResponseResult`](../../doc/models/entity-custom-fields-response-result.md).

## Example Usage

```python
id = 't1_ecf_67d3ab7bc5e308c4815100z'

request_token = '20250423-yourmerchant-refunds-001'

result = entities_custom_fields_controller.get_entity_custom_fields_id(
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
        "id": "t1_ecf_67d3ab7bc5e308c4815100z",
        "created": "2025-03-14 00:07:23.8236",
        "modified": "2025-03-14 00:07:23.8236",
        "creator": "t1_log_67327b89589de7a6d89a665",
        "modifier": "t1_log_67327b89589de7a6d89a665",
        "entity": "t1_ent_67d3ab7bc0ef1d4284d4578",
        "key": "companyId",
        "value": "70bbd35e-8500-f011-90cb-6045bdc7c168",
        "deleted": "2025-03-14 00:07:23"
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


# Put Entity Custom Fields Id

Update an Entity Custom Field.
Custom Fields can be added to entities associated by the Entity Id.
An Entity Id can have various fields associated to it.

```python
def put_entity_custom_fields_id(self,
                               id,
                               body,
                               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `body` | [`EntityCustomFieldsPutRequest`](../../doc/models/entity-custom-fields-put-request.md) | Body, Required | - |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityCustomFieldsResponseResult`](../../doc/models/entity-custom-fields-response-result.md).

## Example Usage

```python
id = 't1_ecf_67d3ab7bc5e308c4815100z'

body = EntityCustomFieldsPutRequest(
    key='companyId',
    value='70bbd35e-8500-f011-90cb-6045bdc7c168'
)

request_token = '20250423-yourmerchant-refunds-001'

result = entities_custom_fields_controller.put_entity_custom_fields_id(
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
        "id": "t1_ecf_67d3ab7bc5e308c4815100z",
        "created": "2025-03-14 00:07:23.8236",
        "modified": "2025-03-14 00:07:23.8236",
        "creator": "t1_log_67327b89589de7a6d89a665",
        "modifier": "t1_log_67327b89589de7a6d89a665",
        "entity": "t1_ent_67d3ab7bc0ef1d4284d4578",
        "key": "companyId",
        "value": "70bbd35e-8500-f011-90cb-6045bdc7c168",
        "deleted": "2025-03-14 00:07:23"
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


# Delete Entity Custom Fields Id

Delete an Entity Custom Field.

```python
def delete_entity_custom_fields_id(self,
                                  id,
                                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this resource. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityCustomFieldsResponseResult`](../../doc/models/entity-custom-fields-response-result.md).

## Example Usage

```python
id = 't1_ecf_67d3ab7bc5e308c4815100z'

request_token = '20250423-yourmerchant-refunds-001'

result = entities_custom_fields_controller.delete_entity_custom_fields_id(
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
        "id": "t1_ecf_67d3ab7bc5e308c4815100z",
        "created": "2025-03-14 00:07:23.8236",
        "modified": "2025-03-14 00:07:23.8236",
        "creator": "t1_log_67327b89589de7a6d89a665",
        "modifier": "t1_log_67327b89589de7a6d89a665",
        "entity": "t1_ent_67d3ab7bc0ef1d4284d4578",
        "key": "companyId",
        "value": "70bbd35e-8500-f011-90cb-6045bdc7c168",
        "deleted": "2025-03-14 00:07:23"
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


# Get Entity Custom Fields

Query an Entity Custom Field.
Custom Fields can be added to entities associated by the Entity Id.
An Entity Id can have various fields associated to it.

```python
def get_entity_custom_fields(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityCustomFieldsResponseResult`](../../doc/models/entity-custom-fields-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = entities_custom_fields_controller.get_entity_custom_fields(
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
        "id": "t1_ecf_67d3ab7bc5e308c4815100z",
        "created": "2025-03-14 00:07:23.8236",
        "modified": "2025-03-14 00:07:23.8236",
        "creator": "t1_log_67327b89589de7a6d89a665",
        "modifier": "t1_log_67327b89589de7a6d89a665",
        "entity": "t1_ent_67d3ab7bc0ef1d4284d4578",
        "key": "companyId",
        "value": "70bbd35e-8500-f011-90cb-6045bdc7c168",
        "deleted": "2025-03-14 00:07:23"
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


# Post Entity Custom Fields

Create an Entity Custom Field. Custom Fields can be added to entities associated by the Entity Id. An Entity Id can have various fields associated to it.

```python
def post_entity_custom_fields(self,
                             body,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`EntityCustomFieldsPostRequest`](../../doc/models/entity-custom-fields-post-request.md) | Body, Required | Add Entity Cutom Field Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`EntityCustomFieldsResponseResult`](../../doc/models/entity-custom-fields-response-result.md).

## Example Usage

```python
body = EntityCustomFieldsPostRequest(
    entity='t1_ent_67d3ab7bc0ef1d4284d4578',
    key='companyId',
    value='70bbd35e-8500-f011-90cb-6045bdc7c168'
)

request_token = '20250423-yourmerchant-refunds-001'

result = entities_custom_fields_controller.post_entity_custom_fields(
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
        "id": "t1_ecf_67d3ab7bc5e308c4815100z",
        "created": "2025-03-14 00:07:23.8236",
        "modified": "2025-03-14 00:07:23.8236",
        "creator": "t1_log_67327b89589de7a6d89a665",
        "modifier": "t1_log_67327b89589de7a6d89a665",
        "entity": "t1_ent_67d3ab7bc0ef1d4284d4578",
        "key": "companyId",
        "value": "70bbd35e-8500-f011-90cb-6045bdc7c168",
        "deleted": "2025-03-14 00:07:23"
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

