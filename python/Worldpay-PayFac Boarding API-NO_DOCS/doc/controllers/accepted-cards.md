# Accepted Cards

```python
accepted_cards_controller = client.accepted_cards
```

## Class Name

`AcceptedCardsController`

## Methods

* [Get Accepted Cards](../../doc/controllers/accepted-cards.md#get-accepted-cards)
* [Add Accepted Card](../../doc/controllers/accepted-cards.md#add-accepted-card)
* [Get Accepted Card](../../doc/controllers/accepted-cards.md#get-accepted-card)
* [Update Accepted Card](../../doc/controllers/accepted-cards.md#update-accepted-card)
* [Delete Accepted Card](../../doc/controllers/accepted-cards.md#delete-accepted-card)


# Get Accepted Cards

URI to get all acceptedcards of a PayFac submerchant. <br/> <br/> ***For AmericanExpress OptBlue and Discover, OptBlue SE AccountNumber or Discover AccountNumber will be returned in the attributes respectively. Amex OptBlue is available for submerchants in both USA and Canada.***

```python
def get_accepted_cards(self,
                      v_correlation_id,
                      id,
                      content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AcceptedCardsGetResponse`](../../doc/models/accepted-cards-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = accepted_cards_controller.get_accepted_cards(
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


# Add Accepted Card

URI to add a new acceptedcard resource to the PayFac submerchant acceptedcards collection. <br/> ***Amex OptBlue is available for submerchants in both USA and Canada.***

```python
def add_accepted_card(self,
                     v_correlation_id,
                     id,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`AcceptedCard`](../../doc/models/accepted-card.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AcceptedCardsTypeGetResponse`](../../doc/models/accepted-cards-type-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = AcceptedCard(
    mtype=Type3Enum.AMERICANEXPRESS
)

result = accepted_cards_controller.add_accepted_card(
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


# Get Accepted Card

URI to get an acceptedcard resource of a PayFac submerchant. <br/> <br/> ***For AmericanExpress OptBlue and Discover, OptBlue SE AccountNumber or Discover AccountNumber will be returned in the attributes respectively.
Amex OptBlue is available for submerchants in both USA and Canada.***

```python
def get_accepted_card(self,
                     v_correlation_id,
                     id,
                     mtype,
                     content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `mtype` | [`Type16Enum`](../../doc/models/type-16-enum.md) | Template, Required | Card Type |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AcceptedCardsTypeGetResponse`](../../doc/models/accepted-cards-type-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type16Enum.AMERICANEXPRESS

content_type = 'application/json'

result = accepted_cards_controller.get_accepted_card(
    v_correlation_id,
    id,
    mtype,
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


# Update Accepted Card

URI to update an accepted card resource of a PayFac submerchant.Please note that all PUT requests are replace requests, and any optional attribute that was provided in the POST(Create) request but missed in the PUT(replace) request will be replaced with a NULL value. <br/> ***Amex OptBlue is available for submerchants in both USA and Canada.***

```python
def update_accepted_card(self,
                        v_correlation_id,
                        id,
                        mtype,
                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `mtype` | [`Type16Enum`](../../doc/models/type-16-enum.md) | Template, Required | Card Type |
| `body` | [`AcceptedCardForUpdate`](../../doc/models/accepted-card-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AcceptedCardsTypeGetResponse`](../../doc/models/accepted-cards-type-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type16Enum.AMERICANEXPRESS

body = AcceptedCardForUpdate()

result = accepted_cards_controller.update_accepted_card(
    v_correlation_id,
    id,
    mtype,
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
| 403 | Forbidden | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Delete Accepted Card

URI to remove an accepted card resource of a PayFac submerchant. <br/> ***Amex OptBlue is available for submerchants in both USA and Canada.***

```python
def delete_accepted_card(self,
                        v_correlation_id,
                        id,
                        mtype,
                        content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `mtype` | [`Type18Enum`](../../doc/models/type-18-enum.md) | Template, Required | Card Type |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type18Enum.DEBIT

content_type = 'application/json'

result = accepted_cards_controller.delete_accepted_card(
    v_correlation_id,
    id,
    mtype,
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

