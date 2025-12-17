# Chargeback Documents

```python
chargeback_documents_controller = client.chargeback_documents
```

## Class Name

`ChargebackDocumentsController`

## Methods

* [Get Chargeback Documents Id](../../doc/controllers/chargeback-documents.md#get-chargeback-documents-id)
* [Put Chargeback Documents Id](../../doc/controllers/chargeback-documents.md#put-chargeback-documents-id)
* [Delete Chargeback Documents Id](../../doc/controllers/chargeback-documents.md#delete-chargeback-documents-id)
* [Get Chargeback Documents](../../doc/controllers/chargeback-documents.md#get-chargeback-documents)
* [Post Chargeback Documents](../../doc/controllers/chargeback-documents.md#post-chargeback-documents)


# Get Chargeback Documents Id

Query a chargebackDocument. A chargebackDocument resource represents a file related to a Chargeback.

```python
def get_chargeback_documents_id(self,
                               id,
                               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this chargeback document. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackDocumentsResponseResult`](../../doc/models/chargeback-documents-response-result.md).

## Example Usage

```python
id = 't1_chd_679a4a2ba49405540af4856'

request_token = '20250423-yourmerchant-refunds-001'

result = chargeback_documents_controller.get_chargeback_documents_id(
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
        "id": "p1_chd_67b31fca23feed2b88d8a59",
        "created": "2025-02-17 06:38:50.1502",
        "modified": "2025-02-17 06:38:50.1502",
        "creator": "t1_log_5d49bbb9bd62b95c1378542",
        "modifier": "t1_log_5d49bbb9bd62b95c1378542",
        "chargeback": "t1_chb_679918b34232ae6145ec03e",
        "ref": "p1_chd_67b31fca23feed2b88d8a59.pdf",
        "type": "pdf",
        "name": "Test PDF  copy.pdf",
        "description": "Test PDF  copy.pdf",
        "inactive": 0,
        "frozen": 0,
        "status": "created",
        "documentSource": "merchant"
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


# Put Chargeback Documents Id

Update a chargebackDocument. A chargebackDocument resource represents a file related to a Chargeback.

```python
def put_chargeback_documents_id(self,
                               id,
                               body,
                               request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this chargeback document. |
| `body` | [`ChargebacksDocumentsPutRequest`](../../doc/models/chargebacks-documents-put-request.md) | Body, Required | Update Chargeback Document Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackDocumentsResponseResult`](../../doc/models/chargeback-documents-response-result.md).

## Example Usage

```python
id = 't1_chd_679a4a2ba49405540af4856'

body = ChargebacksDocumentsPutRequest(
    mtype=ChargebackDocumentTypeEnum.PDF,
    ref='p1_chd_67b31fca23feed2b88d8a59.pdf',
    description='Test PDF  copy.pdf',
    name='Test PDF  copy.pdf',
    document_source=DocumentSourceEnum.MERCHANT,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN
)

request_token = '20250423-yourmerchant-refunds-001'

result = chargeback_documents_controller.put_chargeback_documents_id(
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
        "id": "p1_chd_67b31fca23feed2b88d8a59",
        "created": "2025-02-17 06:38:50.1502",
        "modified": "2025-02-17 06:38:50.1502",
        "creator": "t1_log_5d49bbb9bd62b95c1378542",
        "modifier": "t1_log_5d49bbb9bd62b95c1378542",
        "chargeback": "t1_chb_679918b34232ae6145ec03e",
        "ref": "p1_chd_67b31fca23feed2b88d8a59.pdf",
        "type": "pdf",
        "name": "Test PDF  copy.pdf",
        "description": "Test PDF  copy.pdf",
        "inactive": 0,
        "frozen": 0,
        "status": "created",
        "documentSource": "merchant"
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


# Delete Chargeback Documents Id

Delete a chargebackDocument. A chargebackDocument resource represents a file related to a Chargeback.

```python
def delete_chargeback_documents_id(self,
                                  id,
                                  request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this chargeback document. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackDocumentsResponseResult`](../../doc/models/chargeback-documents-response-result.md).

## Example Usage

```python
id = 't1_chd_679a4a2ba49405540af4856'

request_token = '20250423-yourmerchant-refunds-001'

result = chargeback_documents_controller.delete_chargeback_documents_id(
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
        "id": "p1_chd_67b31fca23feed2b88d8a59",
        "created": "2025-02-17 06:38:50.1502",
        "modified": "2025-02-17 06:38:50.1502",
        "creator": "t1_log_5d49bbb9bd62b95c1378542",
        "modifier": "t1_log_5d49bbb9bd62b95c1378542",
        "chargeback": "t1_chb_679918b34232ae6145ec03e",
        "ref": "p1_chd_67b31fca23feed2b88d8a59.pdf",
        "type": "pdf",
        "name": "Test PDF  copy.pdf",
        "description": "Test PDF  copy.pdf",
        "inactive": 0,
        "frozen": 0,
        "status": "created",
        "documentSource": "merchant"
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


# Get Chargeback Documents

Query chargebackDocuments, each representing a file related to a Chargeback.

```python
def get_chargeback_documents(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackDocumentsResponseResult`](../../doc/models/chargeback-documents-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = chargeback_documents_controller.get_chargeback_documents(
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
        "id": "p1_chd_67b31fca23feed2b88d8a59",
        "created": "2025-02-17 06:38:50.1502",
        "modified": "2025-02-17 06:38:50.1502",
        "creator": "t1_log_5d49bbb9bd62b95c1378542",
        "modifier": "t1_log_5d49bbb9bd62b95c1378542",
        "chargeback": "t1_chb_679918b34232ae6145ec03e",
        "ref": "p1_chd_67b31fca23feed2b88d8a59.pdf",
        "type": "pdf",
        "name": "Test PDF  copy.pdf",
        "description": "Test PDF  copy.pdf",
        "inactive": 0,
        "frozen": 0,
        "status": "created",
        "documentSource": "merchant"
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


# Post Chargeback Documents

Create a chargebackDocument resource that represents a file related to a Chargeback.

```python
def post_chargeback_documents(self,
                             body,
                             request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChargebackDocumentsPostRequest`](../../doc/models/chargeback-documents-post-request.md) | Body, Required | Create Chargeback Document Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackDocumentsResponseResult`](../../doc/models/chargeback-documents-response-result.md).

## Example Usage

```python
body = ChargebackDocumentsPostRequest(
    chargeback='t1_chb_679918b34232ae6145ec03e',
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    mtype=ChargebackDocumentTypeEnum.PDF,
    ref='p1_chd_67b31fca23feed2b88d8a59.pdf',
    description='Test PDF  copy.pdf',
    name='Test PDF  copy.pdf',
    document_source=DocumentSourceEnum.MERCHANT
)

request_token = '20250423-yourmerchant-refunds-001'

result = chargeback_documents_controller.post_chargeback_documents(
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
        "id": "p1_chd_67b31fca23feed2b88d8a59",
        "created": "2025-02-17 06:38:50.1502",
        "modified": "2025-02-17 06:38:50.1502",
        "creator": "t1_log_5d49bbb9bd62b95c1378542",
        "modifier": "t1_log_5d49bbb9bd62b95c1378542",
        "chargeback": "t1_chb_679918b34232ae6145ec03e",
        "ref": "p1_chd_67b31fca23feed2b88d8a59.pdf",
        "type": "pdf",
        "name": "Test PDF  copy.pdf",
        "description": "Test PDF  copy.pdf",
        "inactive": 0,
        "frozen": 0,
        "status": "created",
        "documentSource": "merchant"
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

