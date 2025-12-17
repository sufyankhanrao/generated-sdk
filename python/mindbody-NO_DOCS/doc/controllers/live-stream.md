# Live Stream

```python
live_stream_controller = client.live_stream
```

## Class Name

`LiveStreamController`


# Generate Signed Live Stream Url

Create an encrypted link to VWP live stream for third party integration customer.

:information_source: **Note** This endpoint does not require authentication.

```python
def generate_signed_live_stream_url(self,
                                   version,
                                   request,
                                   site_id,
                                   authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`GenerateSignedLiveStreamUrlRequest`](../../doc/models/generate-signed-live-stream-url-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GenerateSignedLiveStreamUrlResponse`](../../doc/models/generate-signed-live-stream-url-response.md).

## Example Usage

```python
version = '6'

request = GenerateSignedLiveStreamUrlRequest(
    client_id=98,
    subscriber_id=198,
    user_display_name='UserDisplayName6',
    service_id=130,
    api_user='ApiUser2'
)

site_id = '-99'

authorization = 'authorization6'

result = live_stream_controller.generate_signed_live_stream_url(
    version,
    request,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

