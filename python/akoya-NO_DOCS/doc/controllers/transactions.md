# Transactions

Transactions

```python
transactions_api = client.transactions
```

## Class Name

`TransactionsApi`


# Get-Transactions

The transactions API allows you to retrieve transaction history of consumer-permissioned accounts.

> 🛑
> 
> The *id_token* should be used as the bearer token with this call.

For more information on how to paginate transaction results, please see: [Pagination](https://docs.akoya.com/v2/docs/pagination)

Use the `mode` query param to receive FDX-aligned, standardized data values (Beta). For example:

`https://sandbox-products.ddp.akoya.com/transactions/v2/mikomo?mode=standard`

`mode` is available in both sandbox and production.

`mode` is supported by a subset of providers. Log into the [Data Recipient Hub](https://recipient.ddp.akoya.com/login) and click [here](https://recipient.ddp.akoya.com/support/article/kA0Uw00000015GzKAI) to view a list of all providers supporting the `mode` parameter.

```python
def get_transactions(self,
                    version,
                    provider_id,
                    account_id,
                    start_time=None,
                    end_time=None,
                    offset='0',
                    limit=50,
                    x_akoya_interaction_type=None,
                    mode=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `account_id` | `str` | Template, Required | Account Identifier |
| `start_time` | `datetime` | Query, Optional | ISO 8601 date format in UTC time zone. If blank, the default value (current date - 15 calendar days) is used. If a value is specified, endTime is required. |
| `end_time` | `datetime` | Query, Optional | ISO 8601 date format in UTC time zone. If blank, the default value (current date) is used. If a value is specified, startTime is required. |
| `offset` | `str` | Query, Optional | The number of items to skip before the first in the response. The default is 0.<br><br>**Default**: `'0'` |
| `limit` | `int` | Query, Optional | The maximum number of items to be returned in the response. The default is 50.<br><br>**Default**: `50` |
| `x_akoya_interaction_type` | [`InteractionType`](../../doc/models/interaction-type.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |
| `mode` | [`Mode`](../../doc/models/mode.md) | Query, Optional | BETA. Default is raw. Use standard for FDX-aligned, standardized data values. |

## Response Type

This method returns an instance of [`PagedIterable`](../../doc/paged-iterable.md), where each item is of type `Any` and each page is of type [`TransactionsEntity`](../../doc/models/transactions-entity.md).

## Example Usage

```python
version = 'v2'

provider_id = 'mikomo'

account_id = ':accountId'

start_time = dateutil.parser.parse('03/30/2020 04:00:00')

end_time = dateutil.parser.parse('03/30/2021 04:00:00')

offset = '0'

limit = 50

mode = Mode.RAW

result = transactions_api.get_transactions(
    version,
    provider_id,
    account_id,
    start_time=start_time,
    end_time=end_time,
    offset=offset,
    limit=limit,
    mode=mode
)

# Iterating over items in all pages.
try:
    for _item in result:
        print(_item)
except ApiException as e:
    print(e)

# Iterating over pages in the paginated response.
try:
    for _page in result.pages():
        print(_page.body)
        # Iterating over items in the current page.
        for _item in _page.items():
            print(_item)
except ApiException as e:
    print(e)
```

## Example Response *(as JSON)*

```json
{
  "links": {
    "prev": {
      "href": "/transactions/v2/mikomo/33fbd9e5-9cc3-3d7d-15b3-70d97d87ca1d?endTime=2021-02-26T00%3A00%3A00Z&limit=5&offset=0&startTime=2019-02-26T00%3A00%3A00Z"
    }
  },
  "transactions": [
    {
      "depositTransaction": {
        "accountId": "33fbd9e5-9cc3-3d7d-15b3-70d97d87ca1d",
        "amount": 0.29,
        "debitCreditMemo": "CREDIT",
        "description": "Interest Paid This Period",
        "postedTimestamp": "2021-01-27T00:00:00Z",
        "status": "POSTED",
        "transactionId": "22ef95ee-6127-382d-a28c-5b8b7a15d2eb",
        "transactionTimestamp": "2021-01-27T00:00:00Z",
        "transactionType": "INTEREST"
      }
    },
    {
      "depositTransaction": {
        "accountId": "33fbd9e5-9cc3-3d7d-15b3-70d97d87ca1d",
        "amount": 0.13,
        "debitCreditMemo": "CREDIT",
        "description": "Interest Paid This Period",
        "postedTimestamp": "2021-02-24T00:00:00Z",
        "status": "POSTED",
        "transactionId": "f3fced9d-a7a2-4194-5a17-a2a9b09ff64a",
        "transactionTimestamp": "2021-02-24T00:00:00Z",
        "transactionType": "INTEREST"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 401 | Customer not authorized. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | 701 - Tax Lots not found. The `holdingId` may be wrong. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `ApiException` |
| 406 | Content Type not Supported | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 429 | 1207 - Too many requests | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 500 | Catch-all exception where request was not processed due to an internal outage/issue. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 501 | FdxVersion in header is not implemented. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 503 | System is down for maintenance. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

