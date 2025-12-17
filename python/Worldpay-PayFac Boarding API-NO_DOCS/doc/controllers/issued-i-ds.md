# Issued I Ds

```python
issued_i_ds_controller = client.issued_i_ds
```

## Class Name

`IssuedIDsController`

## Methods

* [Get Issued Ids](../../doc/controllers/issued-i-ds.md#get-issued-ids)
* [Add Issued Id](../../doc/controllers/issued-i-ds.md#add-issued-id)
* [Get Issued Id](../../doc/controllers/issued-i-ds.md#get-issued-id)
* [Update Issued Id](../../doc/controllers/issued-i-ds.md#update-issued-id)


# Get Issued Ids

URI to get all IssuedIds for an owner(existing) of a PayFac submerchant.

```python
def get_issued_ids(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IssuedIdsGetResponse`](../../doc/models/issued-ids-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

content_type = 'application/json'

result = issued_i_ds_controller.get_issued_ids(
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


# Add Issued Id

URI to add a new IssuedId for an owner(existing) of a PayFac submerchant.

```python
def add_issued_id(self,
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
| `body` | [`IssuedId`](../../doc/models/issued-id.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IssuedIdsPostResponse`](../../doc/models/issued-ids-post-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

body = IssuedId(
    id_number='1234567',
    id_type=IdTypeEnum.ALIENID,
    issued_city='Anchorage',
    issued_country=IssuedCountryEnum.US
)

result = issued_i_ds_controller.add_issued_id(
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


# Get Issued Id

URI to get an IssuedId for an owner(existing) of a PayFac submerchant.

```python
def get_issued_id(self,
                 v_correlation_id,
                 id,
                 mtype,
                 idtype,
                 content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Template, Required | Ownership Type |
| `idtype` | [`Idtype1Enum`](../../doc/models/idtype-1-enum.md) | Template, Required | ID Type |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IssuedIdsTypeGetResponse`](../../doc/models/issued-ids-type-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

idtype = Idtype1Enum.DRIVERSLICENSE

content_type = 'application/json'

result = issued_i_ds_controller.get_issued_id(
    v_correlation_id,
    id,
    mtype,
    idtype,
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


# Update Issued Id

URI to update an IssuedId for an owner(existing) of a PayFac submerchant.Please note that all PUT requests are replace requests, and any optional attribute that was provided in the POST(Create) request but missed in the PUT(replace) request will be replaced with a NULL value.

```python
def update_issued_id(self,
                    v_correlation_id,
                    id,
                    mtype,
                    idtype,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `mtype` | [`Type5Enum`](../../doc/models/type-5-enum.md) | Template, Required | Ownership Type |
| `idtype` | [`Idtype1Enum`](../../doc/models/idtype-1-enum.md) | Template, Required | ID Type |
| `body` | [`IssuedIdForUpdate`](../../doc/models/issued-id-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`IssuedIdsPostResponse`](../../doc/models/issued-ids-post-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

mtype = Type5Enum.BENEFICIALOWNER9

idtype = Idtype1Enum.DRIVERSLICENSE

body = IssuedIdForUpdate(
    id_number='1234567',
    issued_city='Anchorage',
    issued_country=IssuedCountryEnum.US
)

result = issued_i_ds_controller.update_issued_id(
    v_correlation_id,
    id,
    mtype,
    idtype,
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

