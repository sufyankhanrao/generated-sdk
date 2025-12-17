# Messages

Represents a message within a Message Thread.

```python
messages_controller = client.messages
```

## Class Name

`MessagesController`

## Methods

* [Get Messages Id](../../doc/controllers/messages.md#get-messages-id)
* [Put Messages Id](../../doc/controllers/messages.md#put-messages-id)
* [Get Messages](../../doc/controllers/messages.md#get-messages)
* [Post Messages](../../doc/controllers/messages.md#post-messages)


# Get Messages Id

Query a Message for a messageThreads.

```python
def get_messages_id(self,
                   id,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this message. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MessagesResponseResult`](../../doc/models/messages-response-result.md).

## Example Usage

```python
id = 't1_mtd_10ca1fcf172a9ac47656a21'

request_token = '20250423-yourmerchant-refunds-001'

result = messages_controller.get_messages_id(
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
        "id": "t1_mtd_10ca1fcf172a9ac47656a21",
        "created": "2025-03-07 00:10:39.1099",
        "modified": "2025-03-07 00:10:39.1099",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "messageThread": "t1_mtd_10ca7fcf172a9ac47656a2c",
        "opposingMessage": "",
        "type": "incoming",
        "generated": 1,
        "secure": 1,
        "read": 0,
        "message": "This is a test message"
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


# Put Messages Id

Update a messages or Message resource, which represents a message for a messageThread.

```python
def put_messages_id(self,
                   id,
                   body,
                   request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this message. |
| `body` | [`MessagesPutRequest`](../../doc/models/messages-put-request.md) | Body, Required | Update Message Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MessagesResponseResult`](../../doc/models/messages-response-result.md).

## Example Usage

```python
id = 't1_mtd_10ca1fcf172a9ac47656a21'

body = MessagesPutRequest(
    read=MessagesReadEnum.READ
)

request_token = '20250423-yourmerchant-refunds-001'

result = messages_controller.put_messages_id(
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
        "id": "t1_mtd_10ca1fcf172a9ac47656a21",
        "created": "2025-03-07 00:10:39.1099",
        "modified": "2025-03-07 00:10:39.1099",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "messageThread": "t1_mtd_10ca7fcf172a9ac47656a2c",
        "opposingMessage": "",
        "type": "incoming",
        "generated": 1,
        "secure": 1,
        "read": 0,
        "message": "This is a test message"
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


# Get Messages

Query a Message or query a messages resource that represents a message for a messageThreads.

```python
def get_messages(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MessagesResponseResult`](../../doc/models/messages-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = messages_controller.get_messages(
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
        "id": "t1_mtd_10ca1fcf172a9ac47656a21",
        "created": "2025-03-07 00:10:39.1099",
        "modified": "2025-03-07 00:10:39.1099",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "messageThread": "t1_mtd_10ca7fcf172a9ac47656a2c",
        "opposingMessage": "",
        "type": "incoming",
        "generated": 1,
        "secure": 1,
        "read": 0,
        "message": "This is a test message"
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


# Post Messages

Create a Messages resource, which represents a message for a messageThread.

```python
def post_messages(self,
                 body,
                 request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MessagesPostRequest`](../../doc/models/messages-post-request.md) | Body, Required | Create Message Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MessagesResponseResult`](../../doc/models/messages-response-result.md).

## Example Usage

```python
body = MessagesPostRequest(
    message_thread='t1_mtd_10ca1fcf172a9ac47656a21',
    secure=SecureEnum.DISPLAYED,
    read=MessagesReadEnum.UNREAD,
    message='This is a test message'
)

request_token = '20250423-yourmerchant-refunds-001'

result = messages_controller.post_messages(
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
        "id": "t1_mtd_10ca1fcf172a9ac47656a21",
        "created": "2025-03-07 00:10:39.1099",
        "modified": "2025-03-07 00:10:39.1099",
        "creator": "t1_log_0092b50e8812b18e41d511s",
        "modifier": "t1_log_0092b50e8812b18e41d511s",
        "messageThread": "t1_mtd_10ca7fcf172a9ac47656a2c",
        "opposingMessage": "",
        "type": "incoming",
        "generated": 1,
        "secure": 1,
        "read": 0,
        "message": "This is a test message"
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

