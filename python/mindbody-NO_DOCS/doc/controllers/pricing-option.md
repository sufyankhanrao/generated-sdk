# Pricing Option

```python
pricing_option_controller = client.pricing_option
```

## Class Name

`PricingOptionController`


# Update Pricing Option

Update Pricing Option data such as name, details, price, discontinued using PricingOptionId(product id)

:information_source: **Note** This endpoint does not require authentication.

```python
def update_pricing_option(self,
                         version,
                         request,
                         site_id,
                         authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdatePricingOptionRequest`](../../doc/models/update-pricing-option-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
version = '6'

request = UpdatePricingOptionRequest(
    product_id=16.72,
    name='Name6',
    price=195.96,
    online_price=230.48,
    count=242,
    sell_online=False
)

site_id = '-99'

authorization = 'authorization6'

result = pricing_option_controller.update_pricing_option(
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

