# Webhooks API

```python
webhooks_api_controller = client.webhooks_api
```

## Class Name

`WebhooksAPIController`

## Methods

* [List All Webhook Channels](../../doc/controllers/webhooks-api.md#list-all-webhook-channels)
* [Get Webhook Channel Details](../../doc/controllers/webhooks-api.md#get-webhook-channel-details)
* [Update Webhook Channel](../../doc/controllers/webhooks-api.md#update-webhook-channel)
* [Reactivate Webhook Channel](../../doc/controllers/webhooks-api.md#reactivate-webhook-channel)
* [Delete Webhook Channel](../../doc/controllers/webhooks-api.md#delete-webhook-channel)
* [Create Webhook Channel](../../doc/controllers/webhooks-api.md#create-webhook-channel)
* [Deactivate Webhook Channel](../../doc/controllers/webhooks-api.md#deactivate-webhook-channel)


# List All Webhook Channels

To get a list of all the webhook channels in the account, use the following call.

```python
def list_all_webhook_channels(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
result = webhooks_api_controller.list_all_webhook_channels()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "total_channel": 3,
  "templatesList": [
    {
      "channelId": 6,
      "companyId": 86,
      "channelName": "channal6",
      "webhookUrl": "https://abc.com/xyz",
      "webhookSecret": "secret6",
      "dateCreated": 1580377929000,
      "webhookLevel": "Account",
      "dateUpdated": 1580377929000,
      "status": "active",
      "eventsSubscribedMap": {
        "folder_sent": true,
        "folder_viewed": true,
        "folder_signed": false,
        "folder_cancelled": true,
        "folder_executed": true,
        "folder_deleted": true
      }
    },
    {
      "channelId": 5,
      "companyId": 86,
      "channelName": "channal5",
      "webhookUrl": "https://qser.com/xyz",
      "webhookSecret": "secret5",
      "dateCreated": 1575970053000,
      "webhookLevel": "Account",
      "dateUpdated": 1576054860000,
      "status": "deactive",
      "eventsSubscribedMap": {
        "folder_sent": true,
        "folder_viewed": true,
        "folder_signed": false,
        "folder_cancelled": true,
        "folder_executed": true,
        "folder_deleted": true
      }
    },
    {
      "channelId": 1,
      "companyId": 86,
      "channelName": "channal1",
      "webhookUrl": "https://aser.com/xyz",
      "webhookSecret": "secret1",
      "dateCreated": 1575530182000,
      "webhookLevel": "API App",
      "dateUpdated": 1580359286000,
      "status": "active",
      "eventsSubscribedMap": {
        "folder_sent": true,
        "folder_viewed": true,
        "folder_signed": true,
        "folder_cancelled": true,
        "folder_executed": true,
        "folder_deleted": true
      }
    }
  ]
}
```


# Get Webhook Channel Details

You can poll our API to get information about a specific Webhook channel.

```python
def get_webhook_channel_details(self,
                               channel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `str` | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
channel_id = '1'

result = webhooks_api_controller.get_webhook_channel_details(channel_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "channel": {
    "channelId": 1,
    "companyId": 86,
    "channelName": "abc",
    "webhookUrl": "https://abc.com/xyz",
    "webhookSecret": "xyz",
    "dateCreated": 1575530182000,
    "webhookLevel": "API App",
    "dateUpdated": 1580359286000,
    "status": "active",
    "eventsSubscribedMap": {
      "folder_sent": true,
      "folder_viewed": true,
      "folder_signed": true,
      "folder_cancelled": true,
      "folder_executed": true,
      "folder_deleted": true
    }
  }
}
```


# Update Webhook Channel

To create a new channel via API, please make a call to /webhook/updatewebhookchannel with the following parameters.

```python
def update_webhook_channel(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookUpdate`](../../doc/models/webhook-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = WebhookUpdate(
    channel_id='1',
    channel_name='updateName',
    webhook_url='https://abc.com/xyz',
    events=WebhookEvents(
        folder_sent=True,
        folder_viewed=True,
        folder_signed=True,
        folder_cancelled=True,
        folder_executed=True,
        folder_deleted=True
    ),
    webhook_secret='updatesecret',
    webhook_level='Account'
)

result = webhooks_api_controller.update_webhook_channel(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "message": "channel successfully updated",
  "channel": {
    "channelId": 1,
    "companyId": 86,
    "channelName": "updateName",
    "webhookUrl": "https://abc.com/xyz",
    "webhookSecret": "updatesecret",
    "dateCreated": 1575530182000,
    "webhookLevel": "Account",
    "dateUpdated": 1580447800000,
    "status": "active",
    "eventsSubscribedMap": {
      "folder_sent": true,
      "folder_cancelled": true,
      "folder_viewed": true,
      "folder_deleted": true,
      "folder_executed": true,
      "folder_signed": true
    }
  }
}
```


# Reactivate Webhook Channel

To create a new channel via API, please make a call to /webhook/updatewebhookchannel with the following parameters.

```python
def reactivate_webhook_channel(self,
                              channel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `str` | Query, Required | Your Channel ID received when creating the webhook. Can also be found in the Foxit eSIgn Settings page. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
channel_id = 'channelId4'

result = webhooks_api_controller.reactivate_webhook_channel(channel_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "templatesList": "channel successfully activated"
}
```


# Delete Webhook Channel

To delete a webhook channel via API, please make a call to this endpoint with the following parameters.

```python
def delete_webhook_channel(self,
                          channel_ids)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_ids` | [`List[WebhookIdentifiers]`](../../doc/models/webhook-identifiers.md) | Body, Required | Your Channel ID received when creating the webhook. Can also be found in the Foxit eSIgn Settings page. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
channel_ids = [
    WebhookIdentifiers(
        channel_ids=[
            2,
            3
        ]
    )
]

result = webhooks_api_controller.delete_webhook_channel(channel_ids)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "webhook channels deleted successfully": [
    2,
    3
  ]
}
```


# Create Webhook Channel

```python
def create_webhook_channel(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`WebhookCreation`](../../doc/models/webhook-creation.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
body = WebhookCreation(
    channel_name='abc',
    webhook_url='https://abc.com/xyz',
    webhook_level='Account',
    events=WebhookEvents(
        folder_sent=True,
        folder_viewed=True,
        folder_signed=False,
        folder_cancelled=True,
        folder_executed=True,
        folder_deleted=True
    ),
    webhook_secret='xyz'
)

result = webhooks_api_controller.create_webhook_channel(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "webhookChannel": {
    "channelId": 6,
    "companyId": 86,
    "channelName": "abc",
    "webhookUrl": "https://abc.com/xyz",
    "webhookSecret": "xyz",
    "dateCreated": null,
    "webhookLevel": "Account",
    "dateUpdated": null,
    "status": "active",
    "eventsSubscribedMap": {
      "folder_sent": true,
      "folder_cancelled": true,
      "folder_viewed": true,
      "folder_deleted": true,
      "folder_executed": true,
      "folder_signed": false
    }
  },
  "message": "channel successfully created"
}
```


# Deactivate Webhook Channel

This endpoint will deactivate your Webhook Channel.

**Note:** To reactivate an channel via API, please make a call to /webhook/channelreactivate

```python
def deactivate_webhook_channel(self,
                              channel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `channel_id` | `str` | Query, Required | Your Channel ID received when creating the webhook. Can also be found in the Foxit eSIgn Settings page. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
channel_id = 'channelId4'

result = webhooks_api_controller.deactivate_webhook_channel(channel_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response

```
{
  "result": "success",
  "templatesList": "channel successfully deactivated"
}
```

