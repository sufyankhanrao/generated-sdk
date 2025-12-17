# VAS-Recurring Billing

```python
vas_recurring_billing_controller = client.vas_recurring_billing
```

## Class Name

`VASRecurringBillingController`

## Methods

* [Get Recurring Billing](../../doc/controllers/vas-recurring-billing.md#get-recurring-billing)
* [Enable Recurring Billing](../../doc/controllers/vas-recurring-billing.md#enable-recurring-billing)
* [Delete Recurring Billing](../../doc/controllers/vas-recurring-billing.md#delete-recurring-billing)


# Get Recurring Billing

URI to get the recurring billing flag of a PayFac submerchant.

```python
def get_recurring_billing(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VasForPassTokenResponse`](../../doc/models/vas-for-pass-token-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = vas_recurring_billing_controller.get_recurring_billing(
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Enable Recurring Billing

URI to enable the recurring billing for a PayFac submerchant. Recurring Billing is tied to PASS token so if PASS token is not enabled before calling recurring billing URI then API will automatically enable PASS token while enabling recurring billing.

```python
def enable_recurring_billing(self,
                            v_correlation_id,
                            id,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`VasForPassToken`](../../doc/models/vas-for-pass-token.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = VasForPassToken()

result = vas_recurring_billing_controller.enable_recurring_billing(
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Delete Recurring Billing

URI to remove a recurring billing resource for a PayFac submerchant.Though recurring billing is tied to PASS token only recurring billing will be deactivated. PASS Token will still be active

```python
def delete_recurring_billing(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`VasForPassTokenResponse`](../../doc/models/vas-for-pass-token-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = vas_recurring_billing_controller.delete_recurring_billing(
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
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |

