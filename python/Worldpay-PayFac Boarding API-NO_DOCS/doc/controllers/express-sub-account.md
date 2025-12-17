# Express Sub-Account

```python
express_sub_account_controller = client.express_sub_account
```

## Class Name

`ExpressSubAccountController`

## Methods

* [Get Express Sub Account](../../doc/controllers/express-sub-account.md#get-express-sub-account)
* [Update Express Sub Account](../../doc/controllers/express-sub-account.md#update-express-sub-account)
* [Add Express Sub Account](../../doc/controllers/express-sub-account.md#add-express-sub-account)


# Get Express Sub Account

URI to get the express subaccount information of a PayFac submerchant.

```python
def get_express_sub_account(self,
                           v_correlation_id,
                           id,
                           content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ExpressSubAccountGetResponse`](../../doc/models/express-sub-account-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = express_sub_account_controller.get_express_sub_account(
    v_correlation_id,
    id,
    content_type=content_type
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ErrorResponseException`](../../doc/models/m400-error-response-exception.md) |
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Update Express Sub Account

URI to update the express subaccount information of a PayFac SubMerchant. Please note that all PUT requests are replace requests, and any optional attribute that was provided in the POST(Create) request but missed in the PUT(replace) request will be replaced with a NULL value. <br/> <br/> This is used only for those PayFacs that are already boarded to Express Gateway for transaction processing. You need to create the Express Sub-Account for a Sub-Merchant before processing the transactions. The following sections provide the structure of the request and response for creating the Express Sub-Account for a Sub-Merchant.  <br/> <br/> ***Please ensure that your Sub-Merchant has Physical Address and CustomerService Contact created before using this resource to on-board your Sub-Merchant to Express Gateway.***

```python
def update_express_sub_account(self,
                              v_correlation_id,
                              id,
                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`ExpressSubAccount`](../../doc/models/express-sub-account.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = ExpressSubAccount(
    express_gateway_id=123456,
    batch_close_method=BatchCloseMethodEnum.TIMEINITIATED,
    batch_close_time='20:00:00',
    check_for_duplicate_transactions=CheckForDuplicateTransactionsEnum.YES,
    enable_commercial_card_bin_query=EnableCommercialCardBINQueryEnum.NO
)

result = express_sub_account_controller.update_express_sub_account(
    v_correlation_id,
    id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ErrorResponseException`](../../doc/models/m400-error-response-exception.md) |
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Add Express Sub Account

URI to create the expresssubaccount for a PayFac submerchant.

```python
def add_express_sub_account(self,
                           v_correlation_id,
                           id,
                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`ExpressSubAccount`](../../doc/models/express-sub-account.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ExpressSubAccountPostResponse`](../../doc/models/express-sub-account-post-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = ExpressSubAccount(
    express_gateway_id=123456,
    batch_close_method=BatchCloseMethodEnum.TIMEINITIATED,
    batch_close_time='20:00:00',
    check_for_duplicate_transactions=CheckForDuplicateTransactionsEnum.YES,
    enable_commercial_card_bin_query=EnableCommercialCardBINQueryEnum.NO
)

result = express_sub_account_controller.add_express_sub_account(
    v_correlation_id,
    id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ErrorResponseException`](../../doc/models/m400-error-response-exception.md) |
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |

