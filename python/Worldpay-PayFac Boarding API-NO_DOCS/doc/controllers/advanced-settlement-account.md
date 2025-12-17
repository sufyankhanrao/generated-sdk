# Advanced Settlement Account

```python
advanced_settlement_account_controller = client.advanced_settlement_account
```

## Class Name

`AdvancedSettlementAccountController`

## Methods

* [Get Advanced Settlement Accounts](../../doc/controllers/advanced-settlement-account.md#get-advanced-settlement-accounts)
* [Update Advanced Settlement Account](../../doc/controllers/advanced-settlement-account.md#update-advanced-settlement-account)
* [Add Advanced Settlement Account](../../doc/controllers/advanced-settlement-account.md#add-advanced-settlement-account)
* [Delete Advanced Settlement Account](../../doc/controllers/advanced-settlement-account.md#delete-advanced-settlement-account)


# Get Advanced Settlement Accounts

URI to get all advancedsettlemtaccounts of a PayFac submerchant.

```python
def get_advanced_settlement_accounts(self,
                                    v_correlation_id,
                                    id,
                                    content_type="application/json",
                                    account_number=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |
| `account_number` | `str` | Header, Optional | The unique bank account number |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdvancedSettlementsGetResponse`](../../doc/models/advanced-settlements-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = advanced_settlement_account_controller.get_advanced_settlement_accounts(
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


# Update Advanced Settlement Account

URI to update an advancedsettlementaccount resource of a PayFac SubMerchant.Please note that all PUT requests are replace requests, and any optional attribute that was provided in the POST(Create) request but missed in the PUT(replace) request will be replaced with a NULL value. Please note that the accountNumber cannot be updated via this PUT endpoint. The existing accountNumber has to be sent.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_advanced_settlement_account(self,
                                      v_correlation_id,
                                      account_number,
                                      id,
                                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `account_number` | `str` | Header, Required | The unique bank account number |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`AdvancedSettlementAccount`](../../doc/models/advanced-settlement-account.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdvancedSettlementsAccountNumberGetResponse`](../../doc/models/advanced-settlements-account-number-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

account_number = 'accountNumber2'

id = 'id0'

body = AdvancedSettlementAccount(
    bank_account=BankAccount(
        dda_type=DdaTypeEnum.CHECKING,
        account_number='12345678910',
        routing_number='123456789'
    ),
    settlement_categories=[
        SettlementCategoryEnum.DEBITDEPOSITS,
        SettlementCategoryEnum.CREDITCONVENIENCEFEES
    ],
    one_ach_for_all_categories=OneACHForAllCategoriesEnum.NO,
    one_ach_for_credit_and_debit=OneACHForCreditAndDebitEnum.NO
)

result = advanced_settlement_account_controller.update_advanced_settlement_account(
    v_correlation_id,
    account_number,
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


# Add Advanced Settlement Account

URI to add a new advancedsettlemtaccount resource to the PayFac submerchant advancedsettlemtaccounts collection.

```python
def add_advanced_settlement_account(self,
                                   v_correlation_id,
                                   id,
                                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`AdvancedSettlementAccount`](../../doc/models/advanced-settlement-account.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AdvancedSettlementsGetResponse`](../../doc/models/advanced-settlements-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = AdvancedSettlementAccount(
    bank_account=BankAccount(
        dda_type=DdaTypeEnum.CHECKING,
        account_number='12345678910',
        routing_number='123456789'
    ),
    settlement_categories=[
        SettlementCategoryEnum.DEBITDEPOSITS,
        SettlementCategoryEnum.CREDITCONVENIENCEFEES
    ],
    one_ach_for_all_categories=OneACHForAllCategoriesEnum.NO,
    one_ach_for_credit_and_debit=OneACHForCreditAndDebitEnum.NO
)

result = advanced_settlement_account_controller.add_advanced_settlement_account(
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


# Delete Advanced Settlement Account

URI to delete an advancedsettlementaccount resource of a PayFac SubMerchant.

```python
def delete_advanced_settlement_account(self,
                                      v_correlation_id,
                                      account_number,
                                      id,
                                      content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `account_number` | `str` | Header, Required | The unique bank account number |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

account_number = 'accountNumber2'

id = 'id0'

content_type = 'application/json'

result = advanced_settlement_account_controller.delete_advanced_settlement_account(
    v_correlation_id,
    account_number,
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
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |

