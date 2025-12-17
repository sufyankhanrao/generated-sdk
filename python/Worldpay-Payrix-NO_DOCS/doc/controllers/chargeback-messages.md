# Chargeback Messages

```python
chargeback_messages_controller = client.chargeback_messages
```

## Class Name

`ChargebackMessagesController`

## Methods

* [Get Chargeback Messages Id](../../doc/controllers/chargeback-messages.md#get-chargeback-messages-id)
* [Get Chargeback Messages](../../doc/controllers/chargeback-messages.md#get-chargeback-messages)
* [Post Chargeback Messages](../../doc/controllers/chargeback-messages.md#post-chargeback-messages)


# Get Chargeback Messages Id

Query a chargebackMessage. A chargebackMessage resource represents a message that is sent by a Merchant, processor, or bank in relation to a Chargeback.

```python
def get_chargeback_messages_id(self,
                              id,
                              request_token=None,
                              search=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of this chargeback message. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |
| `search` | `str` | Header, Optional | Set this header to filter or sort the list of resources that the method returns.<br>See [Searches](page:welcome#searches) for detailed information and examples on how to use search header. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackMessagesResponseResult`](../../doc/models/chargeback-messages-response-result.md).

## Example Usage

```python
id = 't1_chm_fd94438bed7d5e80f0000ea'

request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

result = chargeback_messages_controller.get_chargeback_messages_id(
    id,
    request_token=request_token,
    search=search
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
        "id": "t1_chm_fd94438bed7d5e80f0000ea",
        "created": "2019-09-08 22:30:00.0000",
        "modified": "2019-09-08 22:30:00.0000",
        "creator": "t1_log_6564b6476c2015fa1c04ec7",
        "modifier": "t1_log_6564b6476c2015fa1c04ec7",
        "chargeback": "t1_chb_2c2443d86f1c94d3846f85b",
        "date": "20190908",
        "type": "respond",
        "fromQueue": "",
        "toQueue": "",
        "contact": "",
        "amount": 1,
        "currency": "USD",
        "note": "Charge Merchant",
        "status": "processed",
        "inactive": 0,
        "frozen": 0,
        "imported": 1
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


# Get Chargeback Messages

Query a chargebackMessage resource, which represents a message that is sent by a Merchant, processor, or bank in relation to a Chargeback.

```python
def get_chargeback_messages(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackMessagesResponseResult`](../../doc/models/chargeback-messages-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = chargeback_messages_controller.get_chargeback_messages(
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
        "id": "t1_chm_fd94438bed7d5e80f0000ea",
        "created": "2019-09-08 22:30:00.0000",
        "modified": "2019-09-08 22:30:00.0000",
        "creator": "t1_log_6564b6476c2015fa1c04ec7",
        "modifier": "t1_log_6564b6476c2015fa1c04ec7",
        "chargeback": "t1_chb_2c2443d86f1c94d3846f85b",
        "date": "20190908",
        "type": "respond",
        "fromQueue": "",
        "toQueue": "",
        "contact": "",
        "amount": 1,
        "currency": "USD",
        "note": "Charge Merchant",
        "status": "processed",
        "inactive": 0,
        "frozen": 0,
        "imported": 1
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


# Post Chargeback Messages

Create a chargebackMessage. A chargebackMessage resource represents a message that is sent by a Merchant, processor, or bank in relation to a Chargeback.

```python
def post_chargeback_messages(self,
                            body,
                            request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChargebackMessagePostRequest`](../../doc/models/chargeback-message-post-request.md) | Body, Required | Create Chargeback Message Request |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebackMessagesResponseResult`](../../doc/models/chargeback-messages-response-result.md).

## Example Usage

```python
body = ChargebackMessagePostRequest(
    chargeback='t1_chb_2c2443d86f1c94d3846f85b',
    mtype=ChargebackMessageTypeEnum.RESPOND,
    status=ChargebackMessageStatusEnum.PROCESSED,
    imported=ImportedEnum.IMPORTED,
    inactive=InactiveEnum.ACTIVE,
    frozen=FrozenEnum.NOTFROZEN,
    date='20190908',
    from_queue='specifies queue',
    to_queue='specifies queue',
    contact='identifier of Contact',
    amount=1,
    currency=CurrencyEnum.USD,
    note='Charge Merchant'
)

request_token = '20250423-yourmerchant-refunds-001'

result = chargeback_messages_controller.post_chargeback_messages(
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
        "id": "t1_chm_fd94438bed7d5e80f0000ea",
        "created": "2019-09-08 22:30:00.0000",
        "modified": "2019-09-08 22:30:00.0000",
        "creator": "t1_log_6564b6476c2015fa1c04ec7",
        "modifier": "t1_log_6564b6476c2015fa1c04ec7",
        "chargeback": "t1_chb_2c2443d86f1c94d3846f85b",
        "date": "20190908",
        "type": "respond",
        "fromQueue": "",
        "toQueue": "",
        "contact": "",
        "amount": 1,
        "currency": "USD",
        "note": "Charge Merchant",
        "status": "processed",
        "inactive": 0,
        "frozen": 0,
        "imported": 1
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

