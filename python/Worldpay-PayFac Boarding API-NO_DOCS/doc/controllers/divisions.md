# Divisions

Resource to obtain the divisions for a PayFac

```python
divisions_controller = client.divisions
```

## Class Name

`DivisionsController`

## Methods

* [Divisions](../../doc/controllers/divisions.md#divisions)
* [Create Division](../../doc/controllers/divisions.md#create-division)
* [Divisions by Chain](../../doc/controllers/divisions.md#divisions-by-chain)
* [Division by Division Code](../../doc/controllers/divisions.md#division-by-division-code)
* [Update Divisions](../../doc/controllers/divisions.md#update-divisions)
* [Delete Divisions](../../doc/controllers/divisions.md#delete-divisions)
* [Patch Divisions](../../doc/controllers/divisions.md#patch-divisions)


# Divisions

URI to get all the divisions for a PayFac. A list of divisions will only be returned for Payfacs currently using Divisions in their hierarchy. If a PayFac is not using Divisions, this call will still be successful but the response will be empty.

```python
def divisions(self,
             v_correlation_id,
             content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsGetResponse`](../../doc/models/divisions-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

content_type = 'application/json'

result = divisions_controller.divisions(
    v_correlation_id,
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
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Create Division

This URI will create a new Division Code by taking the  Chain Code, Division Name, Contact Data and Address Data as inputs.

```python
def create_division(self,
                   v_correlation_id,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `body` | [`DivisionsToCreate`](../../doc/models/divisions-to-create.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsPostResponse`](../../doc/models/divisions-post-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

body = DivisionsToCreate(
    chain_code='0A1B2C',
    division_name='Division 001'
)

result = divisions_controller.create_division(
    v_correlation_id,
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
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Divisions by Chain

URI to get the all the divisions for a Chain Code. A list of divisions will only be returned for Payfacs currently using Divisions in their hierarchy. If a PayFac is not using Divisions, this call will still be successful but the response will be empty.

```python
def divisions_by_chain(self,
                      v_correlation_id,
                      chain_code,
                      content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The Chain Code a list of divisions will be returned for |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsGetResponse`](../../doc/models/divisions-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

content_type = 'application/json'

result = divisions_controller.divisions_by_chain(
    v_correlation_id,
    chain_code,
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
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Division by Division Code

URI to get the all the relevant information for a specific division Code. If a PayFac is not using Divisions, this call will still be successful but the response will be empty.

```python
def division_by_division_code(self,
                             v_correlation_id,
                             chain_code,
                             division_code,
                             content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The Chain Code for which a list of divisions will be returned |
| `division_code` | `str` | Template, Required | The division code for which the information needs to be returned |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsPostResponse`](../../doc/models/divisions-post-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

division_code = 'divisionCode0'

content_type = 'application/json'

result = divisions_controller.division_by_division_code(
    v_correlation_id,
    chain_code,
    division_code,
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
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Update Divisions

URI to update information of a PayFac Divisions resource.Please note that all PUT requests are replace requests, and any optional attribute that was provided earlier, but missed in the PUT request will be overridden with NULL. This might not be applicable in this particular case as all attributes in this PUT request are mandatory. <br/> ***If the Division code needs to be updated, it can be done using PATCH /submerchants/{id} endpoint with the Division code sent in the request body***

```python
def update_divisions(self,
                    v_correlation_id,
                    chain_code,
                    division_code,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The chain code under which the division name has to be updated |
| `division_code` | `str` | Template, Required | The division code for which the division name has to be updated. |
| `body` | [`DivisionsForUpdate`](../../doc/models/divisions-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsForUpdateResponse`](../../doc/models/divisions-for-update-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

division_code = 'divisionCode0'

body = DivisionsForUpdate(
    division_name='Division 001'
)

result = divisions_controller.update_divisions(
    v_correlation_id,
    chain_code,
    division_code,
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


# Delete Divisions

URI to remove a Division underneath a Chain.

```python
def delete_divisions(self,
                    v_correlation_id,
                    chain_code,
                    division_code,
                    content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The chain code under which the division has to be removed. |
| `division_code` | `str` | Template, Required | The division code |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

division_code = 'divisionCode0'

content_type = 'application/json'

result = divisions_controller.delete_divisions(
    v_correlation_id,
    chain_code,
    division_code,
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


# Patch Divisions

URI to update information of a PayFac Divisions resource. <br/> ***If the Division code needs to be updated for a submerchant, it can be done using PATCH /submerchants/{id} endpoint with the Division code sent in the request body***

```python
def patch_divisions(self,
                   v_correlation_id,
                   chain_code,
                   division_code,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The chain code under which the division name has to be updated |
| `division_code` | `str` | Template, Required | The division code |
| `body` | [`DivisionsForPatch`](../../doc/models/divisions-for-patch.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DivisionsForPatchResponse`](../../doc/models/divisions-for-patch-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

division_code = 'divisionCode0'

body = DivisionsForPatch(
    division_name='Division 001'
)

result = divisions_controller.patch_divisions(
    v_correlation_id,
    chain_code,
    division_code,
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

