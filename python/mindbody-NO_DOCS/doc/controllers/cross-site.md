# Cross Site

```python
cross_site_controller = client.cross_site
```

## Class Name

`CrossSiteController`


# Copy Credit Card

Copies the credit card information from one client to another, regardless of site.
The source and target clients must have the same email address.

:information_source: **Note** This endpoint does not require authentication.

```python
def copy_credit_card(self,
                    version,
                    request,
                    site_id,
                    authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`CopyCreditCardRequest`](../../doc/models/copy-credit-card-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CopyCreditCardResponse`](../../doc/models/copy-credit-card-response.md).

## Example Usage

```python
version = '6'

request = CopyCreditCardRequest(
    source_site_id=42,
    source_client_id='SourceClientId8',
    target_site_id=26,
    target_client_id='TargetClientId8'
)

site_id = '-99'

authorization = 'authorization6'

result = cross_site_controller.copy_credit_card(
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

