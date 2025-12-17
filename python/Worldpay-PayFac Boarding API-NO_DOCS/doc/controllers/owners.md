# Owners

Resources to create and maintain owners information for a PayFac SubMerchant

```python
owners_controller = client.owners
```

## Class Name

`OwnersController`

## Methods

* [Get Owners](../../doc/controllers/owners.md#get-owners)
* [Add Owner](../../doc/controllers/owners.md#add-owner)
* [Get Owner](../../doc/controllers/owners.md#get-owner)
* [Update Owner](../../doc/controllers/owners.md#update-owner)
* [Delete Owner](../../doc/controllers/owners.md#delete-owner)


# Get Owners

URI to get all owners of a PayFac submerchant.

```python
def get_owners(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OwnersGetResponse`](../../doc/models/owners-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = owners_controller.get_owners(
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


# Add Owner

URI to add a new owner to a PayFac submerchant owners collection.

```python
def add_owner(self,
             v_correlation_id,
             id,
             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`Owner`](../../doc/models/owner.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OwnersGetResponse`](../../doc/models/owners-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = Owner(
    first_name='John',
    last_name='Smith',
    phone_number='5135551234',
    email='jsmith@payfacsm.com',
    ownership_percentage=51,
    address_line_1='123 South St',
    city='Anchorage',
    state=StateEnum.WI,
    country=CountryEnum.US,
    postal_code='99501',
    mtype=TypeEnum.CONTROLOWNER,
    title='President',
    middle_initial='S',
    phone_number_ext='5678',
    fax_number='5135551234',
    ssn='123456789',
    dob=dateutil.parser.parse('1948-12-05').date(),
    address_line_2='Apt 500',
    postal_code_extension='1234'
)

result = owners_controller.add_owner(
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


# Get Owner

URI to get an owner from a PayFac submerchant owners collection.

```python
def get_owner(self,
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
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Template, Required | Ownership Type |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OwnersTypeGetResponse`](../../doc/models/owners-type-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

content_type = 'application/json'

result = owners_controller.get_owner(
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


# Update Owner

URI to update an owner information of a PayFac SubMerchant.Please note that all PUT requests are replace requests, and any optional attribute that was provided in the POST(Create) request but missed in the PUT(replace) request will be replaced with a NULL value.

```python
def update_owner(self,
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
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Template, Required | Ownership Type |
| `body` | [`OwnerForUpdate`](../../doc/models/owner-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OwnerForUpdateResponse`](../../doc/models/owner-for-update-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

body = OwnerForUpdate(
    first_name='John',
    last_name='Smith',
    phone_number='5135551234',
    email='jsmith@payfacsm.com',
    ownership_percentage=51,
    address_line_1='123 South St',
    city='Anchorage',
    state=StateEnum.WI,
    country=CountryEnum.US,
    postal_code='postalCode2',
    title='President',
    middle_initial='S',
    phone_number_ext='5678',
    fax_number='5135551234',
    ssn='123456789',
    dob=dateutil.parser.parse('1948-12-05').date(),
    address_line_2='Apt 500',
    postal_code_extension='1234'
)

result = owners_controller.update_owner(
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
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Delete Owner

URI to remove an owner from the owners collection.

```python
def delete_owner(self,
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
| `mtype` | [`Type7Enum`](../../doc/models/type-7-enum.md) | Template, Required | Ownership Type |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type7Enum.BENEFICIALOWNER1

content_type = 'application/json'

result = owners_controller.delete_owner(
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

