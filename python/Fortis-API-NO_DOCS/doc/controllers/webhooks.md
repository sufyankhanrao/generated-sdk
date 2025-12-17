# Webhooks

```python
webhooks_controller = client.webhooks
```

## Class Name

`WebhooksController`

## Methods

* [Create a New Transaction Batch Postback Config](../../doc/controllers/webhooks.md#create-a-new-transaction-batch-postback-config)
* [Create a New Contact Postback Config](../../doc/controllers/webhooks.md#create-a-new-contact-postback-config)
* [Create a New Transaction Postback Config](../../doc/controllers/webhooks.md#create-a-new-transaction-postback-config)
* [Delete a Postback Config](../../doc/controllers/webhooks.md#delete-a-postback-config)
* [Update Transaction Batch Postback Config](../../doc/controllers/webhooks.md#update-transaction-batch-postback-config)
* [Update Contact Postback Config](../../doc/controllers/webhooks.md#update-contact-postback-config)
* [Update Transaction Postback Config](../../doc/controllers/webhooks.md#update-transaction-postback-config)


# Create a New Transaction Batch Postback Config

```python
def create_a_new_transaction_batch_postback_config(self,
                                                  body,
                                                  expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1WebhooksBatchRequest`](../../doc/models/v1-webhooks-batch-request.md) | Body, Required | - |
| `expand` | [`List[Expand106Enum]`](../../doc/models/expand-106-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
body = V1WebhooksBatchRequest(
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    number_of_attempts=1,
    url='https://127.0.0.1/receiver',
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT
)

result = webhooks_controller.create_a_new_transaction_batch_postback_config(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |


# Create a New Contact Postback Config

```python
def create_a_new_contact_postback_config(self,
                                        body,
                                        expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1WebhooksContactRequest`](../../doc/models/v1-webhooks-contact-request.md) | Body, Required | - |
| `expand` | [`List[Expand106Enum]`](../../doc/models/expand-106-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
body = V1WebhooksContactRequest(
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    number_of_attempts=1,
    url='https://127.0.0.1/receiver',
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT
)

result = webhooks_controller.create_a_new_contact_postback_config(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |


# Create a New Transaction Postback Config

```python
def create_a_new_transaction_postback_config(self,
                                            body,
                                            expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`V1WebhooksTransactionRequest`](../../doc/models/v1-webhooks-transaction-request.md) | Body, Required | - |
| `expand` | [`List[Expand106Enum]`](../../doc/models/expand-106-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
body = V1WebhooksTransactionRequest(
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    number_of_attempts=1,
    url='https://127.0.0.1/receiver',
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT
)

result = webhooks_controller.create_a_new_transaction_postback_config(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |


# Delete a Postback Config

```python
def delete_a_postback_config(self,
                            webhook_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_id` | `str` | Template, Required | Postback Config ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
webhook_id = '11e95f8ec39de8fbdb0a4f1a'

result = webhooks_controller.delete_a_postback_config(webhook_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |


# Update Transaction Batch Postback Config

```python
def update_transaction_batch_postback_config(self,
                                            webhook_id,
                                            body,
                                            expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_id` | `str` | Template, Required | Postback Config ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `body` | [`V1WebhooksBatchRequest1`](../../doc/models/v1-webhooks-batch-request-1.md) | Body, Required | - |
| `expand` | [`List[Expand106Enum]`](../../doc/models/expand-106-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
webhook_id = '11e95f8ec39de8fbdb0a4f1a'

body = V1WebhooksBatchRequest1(
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT,
    number_of_attempts=1,
    url='https://127.0.0.1/receiver'
)

result = webhooks_controller.update_transaction_batch_postback_config(
    webhook_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |


# Update Contact Postback Config

```python
def update_contact_postback_config(self,
                                  webhook_id,
                                  body,
                                  expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_id` | `str` | Template, Required | Postback Config ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `body` | [`V1WebhooksContactRequest1`](../../doc/models/v1-webhooks-contact-request-1.md) | Body, Required | - |
| `expand` | [`List[Expand106Enum]`](../../doc/models/expand-106-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
webhook_id = '11e95f8ec39de8fbdb0a4f1a'

body = V1WebhooksContactRequest1(
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT,
    number_of_attempts=1,
    url='https://127.0.0.1/receiver'
)

result = webhooks_controller.update_contact_postback_config(
    webhook_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |


# Update Transaction Postback Config

```python
def update_transaction_postback_config(self,
                                      webhook_id,
                                      body,
                                      expand=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhook_id` | `str` | Template, Required | Postback Config ID<br><br>**Constraints**: *Pattern*: `^(([0-9a-fA-F\-]{24,36})\|(([0-9a-fA-F]{8})-(([0-9a-fA-F]{4}\-){3})([0-9a-fA-F]{12})))$` |
| `body` | [`V1WebhooksTransactionRequest1`](../../doc/models/v1-webhooks-transaction-request-1.md) | Body, Required | - |
| `expand` | [`List[Expand106Enum]`](../../doc/models/expand-106-enum.md) | Query, Optional | Most endpoints in the API have a way to retrieve extra data related to the current record being retrieved. For example, if the API request is for the accountvaults endpoint, and the end user also needs to know which contact the token belongs to, this data can be returned in the accountvaults endpoint request.<br><br>**Constraints**: *Unique Items Required*, *Pattern*: `^[\w]+$` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponseWebhook`](../../doc/models/response-webhook.md).

## Example Usage

```python
webhook_id = '11e95f8ec39de8fbdb0a4f1a'

body = V1WebhooksTransactionRequest1(
    attempt_interval=300,
    basic_auth_username='tester',
    basic_auth_password='Test@522',
    expands='changelogs,tags',
    format=FormatEnum.APIDEFAULT,
    is_active=True,
    location_id='11e95f8ec39de8fbdb0a4f1a',
    on_create=True,
    on_update=True,
    on_delete=True,
    postback_config_id='11e95f8ec39de8fbdb0a4f1a',
    product_transaction_id='11e95f8ec39de8fbdb0a4f1a',
    resource=Resource12Enum.CONTACT,
    number_of_attempts=1,
    url='https://127.0.0.1/receiver'
)

result = webhooks_controller.update_transaction_postback_config(
    webhook_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "type": "Webhook",
  "data": {
    "attempt_interval": 300,
    "basic_auth_username": "username",
    "basic_auth_password": "password",
    "expands": "changelogs,tags",
    "format": "api-default",
    "is_active": true,
    "location_id": "11e95f8ec39de8fbdb0a4f1a",
    "on_create": true,
    "on_update": true,
    "on_delete": true,
    "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
    "product_transaction_id": "11e95f8ec39de8fbdb0a4f1a",
    "resource": "contact",
    "number_of_attempts": 1,
    "url": "https://127.0.0.1/receiver",
    "id": "11e95f8ec39de8fbdb0a4f1a",
    "postback_logs": [
      {
        "id": "11e95f8ec39de8fbdb0a4f1a",
        "postback_config_id": "11e95f8ec39de8fbdb0a4f1a",
        "changelog_id": "11e95f8ec39de8fbdb0a4f1a",
        "next_run_ts": 1422040992,
        "created_ts": 1422040992,
        "model_id": "11e95f8ec39de8fbdb0a4f1a"
      }
    ]
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`Response401tokenException`](../../doc/models/response-401-token-exception.md) |
| 412 | Precondition Failed | [`Response412Exception`](../../doc/models/response-412-exception.md) |

