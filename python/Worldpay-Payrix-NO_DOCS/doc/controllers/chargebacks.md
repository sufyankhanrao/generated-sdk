# Chargebacks

Resources that deal with chargebacks. A chargeback is a dispute of a purchase that has already been charged to an account that can result in a return of funds.

```python
chargebacks_controller = client.chargebacks
```

## Class Name

`ChargebacksController`

## Methods

* [Get Chargebacks Id](../../doc/controllers/chargebacks.md#get-chargebacks-id)
* [Get Chargebacks](../../doc/controllers/chargebacks.md#get-chargebacks)


# Get Chargebacks Id

Query a Chargeback. A Chargeback is the reversal of a Transaction and means that the funds have been returned to their source. The resource for a Chargeback gives details of the Chargeback, including the reason why it occurred and the date when it occurred.

```python
def get_chargebacks_id(self,
                      id,
                      request_token=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The ID of the Chargeback. |
| `request_token` | `str` | Header, Optional | A custom, one-time identifier for any API request (GET, PUT, POST, or DELETE). Blocks future requests with the same token for 48 hours, ensuring only the first request is processed. Valid values can contain 1-100 alphanumeric and special characters. See <a href="/apis/payrix/dev-int-guide/references/request-tokens" target="_blank">Request Tokens</a>  for more information. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebacksResponseResult`](../../doc/models/chargebacks-response-result.md).

## Example Usage

```python
id = 't1_chb_678e573098a7706d87b45c1'

request_token = '20250423-yourmerchant-refunds-001'

result = chargebacks_controller.get_chargebacks_id(
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
        "id": "t1_chb_678e573098a7706d87b45c1",
        "created": "2025-01-20 09:01:20.6435",
        "modified": "2025-01-20 09:09:33.7798",
        "creator": "t1_log_6564b6476c2015fa1c08th9",
        "modifier": "t1_log_6564b6476c2015fa1c08th9",
        "merchant": "t1_mer_66a7dcc35e03d452faa32dc",
        "txn": "t1_txn_678e56d221e81b116dbb452",
        "mid": "01242567",
        "description": "Chargeback for the txn of $200,000",
        "total": 20000,
        "representedTotal": 20000,
        "cycle": "first",
        "currency": "USD",
        "platform": "VANTIV",
        "paymentMethod": 1,
        "ref": "6574367",
        "reason": "No Cardholder Authorization",
        "reasonCode": "4837",
        "issued": 20140815,
        "received": 20140815,
        "reply": 20140919,
        "bankRef": "6574367",
        "chargebackRef": "6574367",
        "status": "open",
        "lastStatusChange": "6574367",
        "actionable": 1,
        "shadow": 0,
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


# Get Chargebacks

Query Chargebacks. A Chargeback is the reversal of a Transaction, meaning that the funds have been returned to their source. The resource for each Chargeback gives details of the Chargeback, including the reason why it occurred and the date when it occurred.

```python
def get_chargebacks(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChargebacksResponseResult`](../../doc/models/chargebacks-response-result.md).

## Example Usage

```python
request_token = '20250423-yourmerchant-refunds-001'

search = 'created[greater]=2025-01-01'

totals = 'count[]=id'

page_number = Liquid error: Value cannot be null. (Parameter 'key')

page_limit = Liquid error: Value cannot be null. (Parameter 'key')

result = chargebacks_controller.get_chargebacks(
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
        "id": "t1_chb_678e573098a7706d87b45c1",
        "created": "2025-01-20 09:01:20.6435",
        "modified": "2025-01-20 09:09:33.7798",
        "creator": "t1_log_6564b6476c2015fa1c08th9",
        "modifier": "t1_log_6564b6476c2015fa1c08th9",
        "merchant": "t1_mer_66a7dcc35e03d452faa32dc",
        "txn": "t1_txn_678e56d221e81b116dbb452",
        "mid": "01242567",
        "description": "Chargeback for the txn of $200,000",
        "total": 20000,
        "representedTotal": 20000,
        "cycle": "first",
        "currency": "USD",
        "platform": "VANTIV",
        "paymentMethod": 1,
        "ref": "6574367",
        "reason": "No Cardholder Authorization",
        "reasonCode": "4837",
        "issued": 20140815,
        "received": 20140815,
        "reply": 20140919,
        "bankRef": "6574367",
        "chargebackRef": "6574367",
        "status": "open",
        "lastStatusChange": "6574367",
        "actionable": 1,
        "shadow": 0,
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

