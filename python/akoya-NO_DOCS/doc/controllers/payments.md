# Payments

Payments

```python
payments_api = client.payments
```

## Class Name

`PaymentsApi`


# Payment-Networks

This product supports use cases such as payment enablement or account opening. The response includes identifiers necessary to make ACH and RTP payments. Identifiers include account number, routing number, identifier type (actual or tokenized account number), and payment network type such as ACH or RTP.

<br>
To see the response schema, select the `200` response below. For an example payload response, see the `200` example response below the *Try it* feature.

> 🛑
> 
> The *id_token* should be used as the bearer token with this call.

```python
def payment_networks(self,
                    version,
                    provider_id,
                    account_id,
                    x_akoya_interaction_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | Akoya major version number. Do not use minor version numbers. For instance, use v2 and not v2.2 |
| `provider_id` | `str` | Template, Required | Id of provider |
| `account_id` | `str` | Template, Required | Account Identifier |
| `x_akoya_interaction_type` | [`InteractionType`](../../doc/models/interaction-type.md) | Header, Optional | Optional but recommended header to include with each data request.<br>Allowed values are `user` or `batch`.<br>`user` indicates a request is prompted by an end-user action.<br>`batch` indicates the request is part of a batch process. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ArrayOfAccountPaymentNetworks`](../../doc/models/array-of-account-payment-networks.md).

## Example Usage

```python
version = 'v2'

provider_id = 'mikomo'

account_id = ':accountId'

result = payments_api.payment_networks(
    version,
    provider_id,
    account_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "paymentNetworks": [
    {
      "bankId": "125000024",
      "identifier": "454992210071",
      "identifierType": "ACCOUNT_NUMBER",
      "type": "US_ACH",
      "transferIn": true,
      "transferOut": true
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Customer not authorized. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 403 | Incorrect providerId or no subscription to provider. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 404 | 701 - Account not found. The `accountId` may be wrong. | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |
| 405 | Method Not Allowed | `ApiException` |
| 408 | Request timed out (round trip call took >10 seconds). | [`ErrorErrorException`](../../doc/models/error-error-exception.md) |

