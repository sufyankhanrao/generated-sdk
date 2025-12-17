# Sale

```python
sale_controller = client.sale
```

## Class Name

`SaleController`

## Methods

* [Get Accepted Card Types](../../doc/controllers/sale.md#get-accepted-card-types)
* [Get Contracts](../../doc/controllers/sale.md#get-contracts)
* [Get Custom Payment Methods](../../doc/controllers/sale.md#get-custom-payment-methods)
* [Get Gift Card Balance](../../doc/controllers/sale.md#get-gift-card-balance)
* [Get Gift Cards](../../doc/controllers/sale.md#get-gift-cards)
* [Get Packages](../../doc/controllers/sale.md#get-packages)
* [Get Products](../../doc/controllers/sale.md#get-products)
* [Update Products](../../doc/controllers/sale.md#update-products)
* [Get Products Inventory](../../doc/controllers/sale.md#get-products-inventory)
* [Get Sales](../../doc/controllers/sale.md#get-sales)
* [Get Services](../../doc/controllers/sale.md#get-services)
* [Update Services](../../doc/controllers/sale.md#update-services)
* [Get Transactions](../../doc/controllers/sale.md#get-transactions)
* [Checkout Shopping Cart](../../doc/controllers/sale.md#checkout-shopping-cart)
* [Initialize Credit Card Entry](../../doc/controllers/sale.md#initialize-credit-card-entry)
* [Purchase Account Credit](../../doc/controllers/sale.md#purchase-account-credit)
* [Purchase Contract](../../doc/controllers/sale.md#purchase-contract)
* [Purchase Gift Card](../../doc/controllers/sale.md#purchase-gift-card)
* [Return Sale](../../doc/controllers/sale.md#return-sale)
* [Update Product Price](../../doc/controllers/sale.md#update-product-price)
* [Update Sale Date](../../doc/controllers/sale.md#update-sale-date)


# Get Accepted Card Types

Gets a list of card types that the site accepts. You can also use `GET Sites` to return the Site object, which contains individual accepted card types for requested sites.

This endpoint has no query parameters.The response returns a list of strings. Possible values are:

* Visa
* MasterCard
* Discover
* AMEX

:information_source: **Note** This endpoint does not require authentication.

```python
def get_accepted_card_types(self,
                           version,
                           site_id,
                           authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `List[str]`.

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.get_accepted_card_types(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Contracts

Returns the contracts and autopay options that are available on a location-by-location basis. Depending on the configurations established by the site, this endpoint returns options that can be used to sign up clients for recurring payments for services offered by the business.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_contracts(self,
                 version,
                 request_location_id,
                 site_id,
                 authorization=None,
                 request_consumer_id=None,
                 request_contract_ids=None,
                 request_limit=None,
                 request_offset=None,
                 request_promo_code=None,
                 request_sold_online=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_location_id` | `int` | Query, Required | The ID of the location that has the requested contracts and AutoPay options. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_consumer_id` | `int` | Query, Optional | The ID of the client. |
| `request_contract_ids` | `List[int]` | Query, Optional | When included, the response only contains details about the specified contract IDs. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_promo_code` | `str` | Query, Optional | PromoCode to apply |
| `request_sold_online` | `bool` | Query, Optional | When `true`, the response only contains details about contracts and AutoPay options that can be sold online.<br>When `false`, all contracts are returned.<br>Default: **false** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetContractsResponse`](../../doc/models/get-contracts-response.md).

## Example Usage

```python
version = '6'

request_location_id = 90

site_id = '-99'

authorization = 'authorization6'

request_consumer_id = 120

request_contract_ids = [
    39,
    40
]

request_limit = 62

request_offset = 100

request_promo_code = 'request.promoCode0'

request_sold_online = False

result = sale_controller.get_contracts(
    version,
    request_location_id,
    site_id,
    authorization=authorization,
    request_consumer_id=request_consumer_id,
    request_contract_ids=request_contract_ids,
    request_limit=request_limit,
    request_offset=request_offset,
    request_promo_code=request_promo_code,
    request_sold_online=request_sold_online
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Custom Payment Methods

Get payment methods that can be used to pay for sales at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_custom_payment_methods(self,
                              version,
                              site_id,
                              authorization=None,
                              request_limit=None,
                              request_offset=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetCustomPaymentMethodsResponse`](../../doc/models/get-custom-payment-methods-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

result = sale_controller.get_custom_payment_methods(
    version,
    site_id,
    authorization=authorization,
    request_limit=request_limit,
    request_offset=request_offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Gift Card Balance

Returns a gift card’s remaining balance.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_gift_card_balance(self,
                         version,
                         site_id,
                         authorization=None,
                         barcode_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `barcode_id` | `str` | Query, Optional | The barcode ID of the gift card for which you want the balance. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetGiftCardBalanceResponse`](../../doc/models/get-gift-card-balance-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

barcode_id = 'barcodeId6'

result = sale_controller.get_gift_card_balance(
    version,
    site_id,
    authorization=authorization,
    barcode_id=barcode_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Gift Cards

Returns information about gift cards that can be purchased.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_gift_cards(self,
                  version,
                  site_id,
                  authorization=None,
                  request_ids=None,
                  request_include_custom_layouts=None,
                  request_limit=None,
                  request_location_id=None,
                  request_offset=None,
                  request_sold_online=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_ids` | `List[int]` | Query, Optional | Filters the results to the requested gift card IDs.<br /><br>Default: **all** gift cards. |
| `request_include_custom_layouts` | `bool` | Query, Optional | When `true`, includes custom gift card layouts.<br /><br>When `false`, includes only system layouts.<br>Default: **false** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | When included, returns gift cards that are sold at the provided location ID. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_sold_online` | `bool` | Query, Optional | When `true`, only returns gift cards that are sold online.<br /><br>Default: **false** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetGiftCardResponse`](../../doc/models/get-gift-card-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_ids = [
    1,
    2
]

request_include_custom_layouts = False

request_limit = 62

request_location_id = 90

request_offset = 100

request_sold_online = False

result = sale_controller.get_gift_cards(
    version,
    site_id,
    authorization=authorization,
    request_ids=request_ids,
    request_include_custom_layouts=request_include_custom_layouts,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_sold_online=request_sold_online
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Packages

A package is typically used to combine multiple services and/or products into a single offering. Staff members can check out multiple appointments while selling the package, and can discount the items included. For example, a spa might bundle a massage, a pedicure, a manicure, a facial, and a few selected beauty products into a package.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_packages(self,
                version,
                site_id,
                authorization=None,
                request_limit=None,
                request_location_id=None,
                request_offset=None,
                request_package_ids=None,
                request_sell_online=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | The location ID to use to determine the tax for the products that this request returns.<br /><br>Default: **online store** |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_package_ids` | `List[int]` | Query, Optional | A list of the packages IDs to filter by. |
| `request_sell_online` | `bool` | Query, Optional | When `true`, only returns products that can be sold online.<br /><br>When `false`, all products are returned.<br /><br>Default: **false** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPackagesResponse`](../../doc/models/get-packages-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_location_id = 90

request_offset = 100

request_package_ids = [
    158,
    159
]

request_sell_online = False

result = sale_controller.get_packages(
    version,
    site_id,
    authorization=authorization,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_package_ids=request_package_ids,
    request_sell_online=request_sell_online
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Products

Get retail products available for purchase at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_products(self,
                version,
                site_id,
                authorization=None,
                request_category_ids=None,
                request_limit=None,
                request_location_id=None,
                request_offset=None,
                request_product_ids=None,
                request_search_text=None,
                request_sell_online=None,
                request_sub_category_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_category_ids` | `List[int]` | Query, Optional | A list of revenue category IDs to filter by. Use this ID when calling the GET Categories endpoint.<br><br>**Note:** The values for these are not currently retrievable through the API. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | The location ID to use to determine the tax for the products that this request returns.<br /><br>Default: **online store** |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_product_ids` | `List[str]` | Query, Optional | The barcode number of the product to be filter by. |
| `request_search_text` | `str` | Query, Optional | A search filter, used for searching by term. |
| `request_sell_online` | `bool` | Query, Optional | When `true`, only products that can be sold online are returned.<br /><br>When `false`, all products are returned.<br /><br>Default: **false** |
| `request_sub_category_ids` | `List[int]` | Query, Optional | A list of subcategory IDs to filter by. Use this ID when calling the GET Categories endpoint.<br><br>**Note:** The values for these are not currently retrievable through the API. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProductsResponse`](../../doc/models/get-products-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_category_ids = [
    140,
    141
]

request_limit = 62

request_location_id = 90

request_offset = 100

request_product_ids = [
    'request.productIds3',
    'request.productIds4'
]

request_search_text = 'request.searchText0'

request_sell_online = False

request_sub_category_ids = [
    173,
    174,
    175
]

result = sale_controller.get_products(
    version,
    site_id,
    authorization=authorization,
    request_category_ids=request_category_ids,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_product_ids=request_product_ids,
    request_search_text=request_search_text,
    request_sell_online=request_sell_online,
    request_sub_category_ids=request_sub_category_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Products

Update retail products available for purchase at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_products(self,
                   version,
                   site_id,
                   update_products_requests,
                   authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `update_products_requests` | [`List[UpdateProductRequest]`](../../doc/models/update-product-request.md) | Body, Required | - |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProductsResponse`](../../doc/models/get-products-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

update_products_requests = [
    UpdateProductRequest(
        barcode_id='BarcodeId2',
        price=47.22,
        online_price=81.74
    ),
    UpdateProductRequest(
        barcode_id='BarcodeId2',
        price=47.22,
        online_price=81.74
    )
]

authorization = 'authorization6'

result = sale_controller.update_products(
    version,
    site_id,
    update_products_requests,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Products Inventory

Get retail products inventory data available at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_products_inventory(self,
                          version,
                          site_id,
                          authorization=None,
                          request_barcode_ids=None,
                          request_limit=None,
                          request_location_ids=None,
                          request_offset=None,
                          request_product_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_barcode_ids` | `List[str]` | Query, Optional | When included, the response only contains details about the specified Barcode Ids. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | When included, the response only contains details about the specified location Ids. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_product_ids` | `List[str]` | Query, Optional | When included, the response only contains details about the specified product Ids. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProductsInventoryResponse`](../../doc/models/get-products-inventory-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_barcode_ids = [
    'request.barcodeIds6'
]

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_product_ids = [
    'request.productIds3',
    'request.productIds4'
]

result = sale_controller.get_products_inventory(
    version,
    site_id,
    authorization=authorization,
    request_barcode_ids=request_barcode_ids,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_product_ids=request_product_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Sales

Get sales completed at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_sales(self,
             version,
             site_id,
             authorization=None,
             request_end_sale_date_time=None,
             request_limit=None,
             request_offset=None,
             request_payment_method_id=None,
             request_sale_id=None,
             request_start_sale_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_sale_date_time` | `datetime` | Query, Optional | Filters results to sales that happened before this date and time. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_payment_method_id` | `int` | Query, Optional | Filters results to sales paid for by the given payment method ID which indicates payment method(s) (i.e. cash, VISA, AMEX, Check, etc.). |
| `request_sale_id` | `int` | Query, Optional | The sale ID associated with the particular item. It Filters results to the requested sale ID. |
| `request_start_sale_date_time` | `datetime` | Query, Optional | Filters results to sales that happened after this date and time. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetSalesResponse`](../../doc/models/get-sales-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_sale_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_payment_method_id = 140

request_sale_id = 32

request_start_sale_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = sale_controller.get_sales(
    version,
    site_id,
    authorization=authorization,
    request_end_sale_date_time=request_end_sale_date_time,
    request_limit=request_limit,
    request_offset=request_offset,
    request_payment_method_id=request_payment_method_id,
    request_sale_id=request_sale_id,
    request_start_sale_date_time=request_start_sale_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Services

Get pricing options available for purchase at a site

:information_source: **Note** This endpoint does not require authentication.

```python
def get_services(self,
                version,
                site_id,
                authorization=None,
                request_class_id=None,
                request_class_schedule_id=None,
                request_hide_related_programs=None,
                request_include_discontinued=None,
                request_include_sale_in_contract_only=None,
                request_limit=None,
                request_location_id=None,
                request_offset=None,
                request_program_ids=None,
                request_sell_online=None,
                request_service_ids=None,
                request_session_type_ids=None,
                request_staff_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_class_id` | `int` | Query, Optional | Filters to the pricing options for the specified class ID. |
| `request_class_schedule_id` | `int` | Query, Optional | Filters to the pricing options for the specified class schedule ID. |
| `request_hide_related_programs` | `bool` | Query, Optional | When `true`, indicates that pricing options of related programs are omitted from the response.<br /><br>Default: **false** |
| `request_include_discontinued` | `bool` | Query, Optional | When `true`, indicates that the filtered pricing option list includes discontinued pricing options.<br /><br>Default: **false** |
| `request_include_sale_in_contract_only` | `bool` | Query, Optional | When `true`, indicates that the filtered pricing option list includes sale in contract only pricing options.<br /><br>Default: **false** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | When specified, for each returned pricing option, `TaxRate` and `TaxIncluded` are calculated according to the specified location. Note that this does not filter results to only services provided at the given location, and for locations where Value-Added Tax (VAT) rules apply, the `TaxRate` is set to zero. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | Filters to pricing options with the specified program IDs. |
| `request_sell_online` | `bool` | Query, Optional | When `true`, filters to the pricing options that can be sold online.<br /><br>Default: **false** |
| `request_service_ids` | `List[str]` | Query, Optional | Filters to the pricing options with the specified IDs. In this context, service and pricing option are used interchangeably. These are the `PurchasedItems[].Id` returned from GET Sales. |
| `request_session_type_ids` | `List[int]` | Query, Optional | Filters to the pricing options with the specified session types IDs. |
| `request_staff_id` | `int` | Query, Optional | Sets `Price` and `OnlinePrice` to the particular pricing of a specific staff member, if allowed by the business. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetServicesResponse`](../../doc/models/get-services-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_id = 206

request_class_schedule_id = 226

request_hide_related_programs = False

request_include_discontinued = False

request_include_sale_in_contract_only = False

request_limit = 62

request_location_id = 90

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_sell_online = False

request_service_ids = [
    'request.serviceIds6',
    'request.serviceIds7',
    'request.serviceIds8'
]

request_session_type_ids = [
    228,
    229
]

request_staff_id = 180

result = sale_controller.get_services(
    version,
    site_id,
    authorization=authorization,
    request_class_id=request_class_id,
    request_class_schedule_id=request_class_schedule_id,
    request_hide_related_programs=request_hide_related_programs,
    request_include_discontinued=request_include_discontinued,
    request_include_sale_in_contract_only=request_include_sale_in_contract_only,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_program_ids=request_program_ids,
    request_sell_online=request_sell_online,
    request_service_ids=request_service_ids,
    request_session_type_ids=request_session_type_ids,
    request_staff_id=request_staff_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Services

Update unit price and online price of provided services.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_services(self,
                   version,
                   site_id,
                   update_services_request,
                   authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `update_services_request` | [`List[UpdateServiceRequest]`](../../doc/models/update-service-request.md) | Body, Required | - |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateServiceResponse`](../../doc/models/update-service-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

update_services_request = [
    UpdateServiceRequest(
        barcode_id='BarcodeId8',
        price=176.98,
        online_price=211.5
    )
]

authorization = 'authorization6'

result = sale_controller.update_services(
    version,
    site_id,
    update_services_request,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Transactions

This endpoint returns a list of transaction details of processed sales.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_transactions(self,
                    version,
                    site_id,
                    authorization=None,
                    request_client_id=None,
                    request_limit=None,
                    request_location_id=None,
                    request_offset=None,
                    request_sale_id=None,
                    request_status=None,
                    request_transaction_end_date_time=None,
                    request_transaction_id=None,
                    request_transaction_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_client_id` | `int` | Query, Optional | Filters results to the requested client ID. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | Filters the transaction results with the ID number associated with the location of the sale. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_sale_id` | `int` | Query, Optional | Filters the transaction results with the ID number associated with the sale. |
| `request_status` | `str` | Query, Optional | Filters the transaction results by the estimated transaction status. |
| `request_transaction_end_date_time` | `datetime` | Query, Optional | Filters the transaction results that happpened before this date and time.<br>Default: **today’s date** |
| `request_transaction_id` | `int` | Query, Optional | Filters the transaction results with the ID number generated when the sale is processed. |
| `request_transaction_start_date_time` | `datetime` | Query, Optional | Filters the transaction results that happpened after this date and time.<br>Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetTransactionsResponse`](../../doc/models/get-transactions-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_client_id = 222

request_limit = 62

request_location_id = 90

request_offset = 100

request_sale_id = 32

request_status = 'request.status2'

request_transaction_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_transaction_id = 200

request_transaction_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = sale_controller.get_transactions(
    version,
    site_id,
    authorization=authorization,
    request_client_id=request_client_id,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_sale_id=request_sale_id,
    request_status=request_status,
    request_transaction_end_date_time=request_transaction_end_date_time,
    request_transaction_id=request_transaction_id,
    request_transaction_start_date_time=request_transaction_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Checkout Shopping Cart

This endpoint provides a wide range of functionality. For example, you can use it when a client purchases new pricing options, retail products, packages, and tips. You can also combine purchasing a new pricing option and many other functions, such as booking a client into a class, booking a new appointment for a client, enrolling a client into an enrollment or course, or reconciling an unpaid, already booked appointment or class. Use this call when a client purchases:

* a pricing option, after calling `GET Services` and choosing a specific pricing option’s ID
* a retail product, after calling `GET Products` and choosing a specific retail product’s ID
* a package, after calling `GET Packages` and choosing a specific package’s ID
* a tip to give to a staff member, after calling `GET Staff` and choosing a specific staff member ID, and the amount that the client wants to tip
  The documentation provides explanations of the request body and response, as well as the cart item metadata, payment item metadata, and purchased cart items.
  This endpoint had been updated to support Strong Customer Authentication (SCA).
  **Note :**
  Protect yourself from processor fees and credit card fraud.Remember to always protect your web forms that leverage POST CheckoutShoppingCart, POST PurchaseContract or POST PurchaseGiftCard with a CAPTCHA!

:information_source: **Note** This endpoint does not require authentication.

```python
def checkout_shopping_cart(self,
                          version,
                          request,
                          site_id,
                          authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`CheckoutShoppingCartRequest`](../../doc/models/checkout-shopping-cart-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CheckoutShoppingCartResponse`](../../doc/models/checkout-shopping-cart-response.md).

## Example Usage

```python
version = '6'

request = CheckoutShoppingCartRequest(
    client_id='ClientId0',
    items=[
        CheckoutItemWrapper(
            item=CheckoutItem(
                mtype='Type2',
                metadata={
                    'key0': {"key1":"val1","key2":"val2"}
                }
            ),
            discount_amount=41.36,
            appointment_booking_requests=[
                CheckoutAppointmentBookingRequest(
                    staff_id=16,
                    location_id=66,
                    session_type_id=166,
                    resources=[
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        )
                    ],
                    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ],
            enrollment_ids=[
                249,
                250
            ],
            class_ids=[
                153,
                154,
                155
            ]
        ),
        CheckoutItemWrapper(
            item=CheckoutItem(
                mtype='Type2',
                metadata={
                    'key0': {"key1":"val1","key2":"val2"}
                }
            ),
            discount_amount=41.36,
            appointment_booking_requests=[
                CheckoutAppointmentBookingRequest(
                    staff_id=16,
                    location_id=66,
                    session_type_id=166,
                    resources=[
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        )
                    ],
                    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ],
            enrollment_ids=[
                249,
                250
            ],
            class_ids=[
                153,
                154,
                155
            ]
        ),
        CheckoutItemWrapper(
            item=CheckoutItem(
                mtype='Type2',
                metadata={
                    'key0': {"key1":"val1","key2":"val2"}
                }
            ),
            discount_amount=41.36,
            appointment_booking_requests=[
                CheckoutAppointmentBookingRequest(
                    staff_id=16,
                    location_id=66,
                    session_type_id=166,
                    resources=[
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        ),
                        ResourceSlim(
                            id=216,
                            name='Name6'
                        )
                    ],
                    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
                )
            ],
            enrollment_ids=[
                249,
                250
            ],
            class_ids=[
                153,
                154,
                155
            ]
        )
    ],
    payments=[
        CheckoutPaymentInfo(
            mtype='Type8',
            metadata={
                'key0': {"key1":"val1","key2":"val2"},
                'key1': {"key1":"val1","key2":"val2"}
            }
        ),
        CheckoutPaymentInfo(
            mtype='Type8',
            metadata={
                'key0': {"key1":"val1","key2":"val2"},
                'key1': {"key1":"val1","key2":"val2"}
            }
        ),
        CheckoutPaymentInfo(
            mtype='Type8',
            metadata={
                'key0': {"key1":"val1","key2":"val2"},
                'key1': {"key1":"val1","key2":"val2"}
            }
        )
    ],
    cart_id='CartId0',
    test=False,
    in_store=False,
    calculate_tax=False,
    promotion_code='PromotionCode2'
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.checkout_shopping_cart(
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


# Initialize Credit Card Entry

**Note**:  
Referer is a DomainURL which will be automatically reflected if the Card UI is loaded via your application.
If you are using this endpoint via postman then you need to specify your domain URL under Referer.

:information_source: **Note** This endpoint does not require authentication.

```python
def initialize_credit_card_entry(self,
                                version,
                                request,
                                site_id,
                                authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`InitializeCreditCardEntryRequest`](../../doc/models/initialize-credit-card-entry-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`InitializeCreditCardEntryResponse`](../../doc/models/initialize-credit-card-entry-response.md).

## Example Usage

```python
version = '6'

request = InitializeCreditCardEntryRequest(
    merchant_account_id='MerchantAccountId4',
    location_id=238
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.initialize_credit_card_entry(
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


# Purchase Account Credit

Allows a client to purchase account credit from a business.

:information_source: **Note** This endpoint does not require authentication.

```python
def purchase_account_credit(self,
                           version,
                           request,
                           site_id,
                           authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`PurchaseAccountCreditRequest`](../../doc/models/purchase-account-credit-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PurchaseAccountCreditResponse`](../../doc/models/purchase-account-credit-response.md).

## Example Usage

```python
version = '6'

request = PurchaseAccountCreditRequest(
    client_id='ClientId0',
    test=False,
    location_id=238,
    send_email_receipt=False,
    sales_rep_id=232,
    consumer_present=False
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.purchase_account_credit(
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


# Purchase Contract

Allows a client to sign up for a contract or autopay using the information returned from the `GET Contracts` endpoint. The client can pay with a new credit card or with a stored credit card. The client must exist at the site specified before this call is made.

This endpoint allows a developer to specify whether a client pays now or pays on the `StartDate`.If you are building a client-facing experience, you should talk with the business owner to understand the owner’s policies before you give clients a choice of the two payment types.
This endpoint had been updated to support Strong Customer Authentication (SCA).

**Note**
Protect yourself from processor fees and credit card fraud. Remember to always protect your web forms that leverage POST CheckoutShoppingCart, POST PurchaseContract or POST PurchaseGiftCard with a CAPTCHA!

:information_source: **Note** This endpoint does not require authentication.

```python
def purchase_contract(self,
                     version,
                     request,
                     site_id,
                     authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`PurchaseContractRequest`](../../doc/models/purchase-contract-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PurchaseContractResponse`](../../doc/models/purchase-contract-response.md).

## Example Usage

```python
version = '6'

request = PurchaseContractRequest(
    client_id='ClientId0',
    contract_id=168,
    test=False,
    location_id=238,
    start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    first_payment_occurs='FirstPaymentOccurs0',
    client_signature='ClientSignature4'
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.purchase_contract(
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


# Purchase Gift Card

Allows a client to purchase a gift card from a business in a variety of designs. The card can be emailed to the recipient on a specific day, and a card title and a personal message can be added.
**Note**
Protect yourself from processor fees and credit card fraud.Remember to always protect your web forms that leverage POST CheckoutShoppingCart, POST PurchaseContract or POST PurchaseGiftCard with a CAPTCHA!

:information_source: **Note** This endpoint does not require authentication.

```python
def purchase_gift_card(self,
                      version,
                      request,
                      site_id,
                      authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`PurchaseGiftCardRequest`](../../doc/models/purchase-gift-card-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PurchaseGiftCardResponse`](../../doc/models/purchase-gift-card-response.md).

## Example Usage

```python
version = '6'

request = PurchaseGiftCardRequest(
    location_id=238,
    purchaser_client_id='PurchaserClientId6',
    gift_card_id=222,
    test=False,
    layout_id=220,
    send_email_receipt=False,
    recipient_email='RecipientEmail2',
    recipient_name='RecipientName2'
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.purchase_gift_card(
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


# Return Sale

Return a comped sale for a specified sale ID in business mode. The sale is returnable only if it is a sale of a service, product or gift card and it has not been used. Currently, only the comp payment method is supported.

:information_source: **Note** This endpoint does not require authentication.

```python
def return_sale(self,
               version,
               return_sale_request,
               site_id,
               authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `return_sale_request` | [`ReturnSaleRequest`](../../doc/models/return-sale-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ReturnSaleResponse`](../../doc/models/return-sale-response.md).

## Example Usage

```python
version = '6'

return_sale_request = ReturnSaleRequest(
    sale_id=6,
    return_reason='ReturnReason8'
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.return_sale(
    version,
    return_sale_request,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Update Product Price

This endpoint updates the retail price and an online price for a product. Passing at least one of them is mandatory.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_product_price(self,
                        version,
                        request,
                        site_id,
                        authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateProductPriceRequest`](../../doc/models/update-product-price-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateProductPriceResponse`](../../doc/models/update-product-price-response.md).

## Example Usage

```python
version = '6'

request = UpdateProductPriceRequest(
    barcode_id='BarcodeId6',
    price=195.96,
    online_price=230.48
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.update_product_price(
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


# Update Sale Date

This endpoint updates the SaleDate and returns the details of the sale.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_sale_date(self,
                    version,
                    request,
                    site_id,
                    authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateSaleDateRequest`](../../doc/models/update-sale-date-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateSaleDateResponse`](../../doc/models/update-sale-date-response.md).

## Example Usage

```python
version = '6'

request = UpdateSaleDateRequest(
    sale_id=232,
    sale_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

site_id = '-99'

authorization = 'authorization6'

result = sale_controller.update_sale_date(
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

