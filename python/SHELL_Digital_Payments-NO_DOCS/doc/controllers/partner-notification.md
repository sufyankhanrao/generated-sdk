# Partner Notification

```python
partner_notification_controller = client.partner_notification
```

## Class Name

`PartnerNotificationController`

## Methods

* [Partner Token](../../doc/controllers/partner-notification.md#partner-token)
* [Finalise Fueling](../../doc/controllers/partner-notification.md#finalise-fueling)
* [Cancel Fueling](../../doc/controllers/partner-notification.md#cancel-fueling)


# Partner Token

To access the Partner’s endpoints, for sending callback messages, Shell will need to connect to the Partner API end points. It is recemmended that the partner offers OAuth 2.0 as a standard for call back APIs and will require the OAuth 2.0 token for authentication. Note this needs to be implemented over HTTPS

:information_source: **Note** This endpoint does not require authentication.

```python
def partner_token(self,
                 grant_type,
                 client_id,
                 client_secret)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `grant_type` | `str` | Form, Required | In OAuth 2.0, the term grant typee refers to the way an application gets an access token. OAuth 2.0 defines several grant types, including the authorization code flow. |
| `client_id` | `str` | Form, Required | After registering your app, you will receive a client ID and a client secret. The client ID is considered public information, and is used to build login URLs, or included in Javascript source code on a page. |
| `client_secret` | `str` | Form, Required | After registering your app, you will receive a client ID and a client secret. The client ID is considered public information, and is used to build login URLs, or included in Javascript source code on a page. The client secret must be kept confidential. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AccessTokenResponse`](../../doc/models/access-token-response.md).

## Example Usage

```python
grant_type = 'client_credentials'

client_id = 'SOFflRakNlwnWlxfOXQ4GHDVyqGawuKA'

client_secret = 'cRnWgw7gACqM3gVS'

result = partner_notification_controller.partner_token(
    grant_type,
    client_id,
    client_secret
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`AccessTokenErrorException`](../../doc/models/access-token-error-exception.md) |


# Finalise Fueling

Enables Shell to inform partner of the successful completion of a transaction. Note this needs to be implemented over HTTPS

:information_source: **Note** This endpoint does not require authentication.

```python
def finalise_fueling(self,
                    body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FinaliseFuelingRequest`](../../doc/models/finalise-fueling-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
body = FinaliseFuelingRequest(
    site_name='Pentahof Site B 9997',
    timestamp=1548429960631,
    volume_quantity=10.4,
    volume_unit='LTR',
    final_price=23.3,
    currency='GBP',
    status='FINISHED',
    site_address='Test Geman Address',
    original_price=23.3,
    discount=0,
    mpp_transaction_id='000000006KCC'
)

result = partner_notification_controller.finalise_fueling(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 401 | Unauthorized | `APIException` |


# Cancel Fueling

Enables Shell to inform partner that a Mobile Payment transaction has been cancelled by Shell as an error/issue occured. Note this needs to be implemented over HTTPS

:information_source: **Note** This endpoint does not require authentication.

```python
def cancel_fueling(self,
                  body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CancelFuelingRequest`](../../doc/models/cancel-fueling-request.md) | Body, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
body = CancelFuelingRequest(
    mpp_transaction_id='000000001E5M',
    reason_code='CANCELLED'
)

result = partner_notification_controller.cancel_fueling(
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | `APIException` |
| 401 | Unauthorized | `APIException` |

