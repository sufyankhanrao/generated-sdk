# Sub Merchant

Resources to create and maintain SubMerchants.

```python
sub_merchant_controller = client.sub_merchant
```

## Class Name

`SubMerchantController`

## Methods

* [Create Submerchant](../../doc/controllers/sub-merchant.md#create-submerchant)
* [Find Submerchants](../../doc/controllers/sub-merchant.md#find-submerchants)
* [Find Submerchants VAS](../../doc/controllers/sub-merchant.md#find-submerchants-vas)
* [Get Submerchant](../../doc/controllers/sub-merchant.md#get-submerchant)
* [Update Submerchant](../../doc/controllers/sub-merchant.md#update-submerchant)
* [Delete Submerchant](../../doc/controllers/sub-merchant.md#delete-submerchant)
* [Patch Submerchant](../../doc/controllers/sub-merchant.md#patch-submerchant)


# Create Submerchant

URI to add a new PayFac submerchant resource to submerchants collection. <br/> When you create a sub-merchant the Boarding Interface will auto-enable the following VAS if they are enabled at the Chain Code level:

* PIN Debit
* PINless Debit

PIN - Personal Identification Number

```python
def create_submerchant(self,
                      v_correlation_id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `body` | [`SubMerchant`](../../doc/models/sub-merchant.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubMerchantsPostResponse`](../../doc/models/sub-merchants-post-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

body = SubMerchant(
    uuid='00001d76-0000-0000-0000-000000000000',
    chain_code='0A1B2C',
    federal_tax_id='123456789',
    legal_name='PayFac_Submerchant 01',
    dba_name='PayFac Submerchant 01',
    billing_descriptor='PFA*SM',
    ownership_type=OwnershipTypeEnum.PUBLICCORPORATION,
    business_type=BusinessTypeEnum.LODGING,
    mcc_code='1520',
    business_established_date=dateutil.parser.parse('2016-03-13').date(),
    transaction_type=TransactionTypeEnum.ONLINESTORE,
    contacts=[
        Contact(
            first_name='Jane',
            last_name='Smith',
            phone_number='5135559876',
            email='jasmith@payfacsm.com',
            mtype=Type1Enum.PRIMARY,
            title='Relationship Manager',
            middle_initial='S',
            phone_number_ext='5432',
            fax_number='5135559876'
        )
    ],
    addresses=[
        Address(
            address_line_1='100 West St',
            city='Anchorage',
            state=StateEnum.GA,
            country=CountryEnum.US,
            postal_code='99501',
            mtype=Type2Enum.MAILING,
            address_line_2='Suite 200',
            postal_code_extension='5555'
        )
    ],
    accepted_cards=[
        AcceptedCard(
            mtype=Type3Enum.AMERICANEXPRESS
        )
    ],
    default_bank_account=BankAccount(
        dda_type=DdaTypeEnum.CHECKING,
        account_number='12345678910',
        routing_number='123456789'
    ),
    division_code='001',
    store_number='000000001',
    website_url='https://payfacsm.com'
)

result = sub_merchant_controller.create_submerchant(
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


# Find Submerchants

Find sub-merchants boarded.Date range cannot exceed 90 days between fromCreatedDate and toCreatedDate.

```python
def find_submerchants(self,
                     v_correlation_id,
                     chain_code,
                     from_created_date,
                     to_created_date,
                     content_type='application/json',
                     sort_by=None,
                     sort_order=None,
                     limit=None,
                     offset=None,
                     underwriting_status=None,
                     division_code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The Chain Code a list of submerchants will be returned for |
| `from_created_date` | `date` | Query, Required | Filter by when the sub-merchant was created |
| `to_created_date` | `date` | Query, Required | Filter by when the sub-merchant was created |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |
| `sort_by` | [`SortByEnum`](../../doc/models/sort-by-enum.md) | Query, Optional | Sort by certain value |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort in ascending or descending order |
| `limit` | `int` | Query, Optional | Limit of Sub-Merchants to respond. Maximum limit is 10. |
| `offset` | `int` | Query, Optional | Row number by which to begin the list (e.g. 10 would start with 10th submerchant) |
| `underwriting_status` | [`UnderwritingStatus1Enum`](../../doc/models/underwriting-status-1-enum.md) | Query, Optional | Look up submerchnats by underwriting status |
| `division_code` | `str` | Query, Optional | Division Code. Only applicable for PayFacs that are using Divisions. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[SubMerchantsFindGetResponse]`](../../doc/models/sub-merchants-find-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

from_created_date = dateutil.parser.parse('2016-03-13').date()

to_created_date = dateutil.parser.parse('2016-03-13').date()

content_type = 'application/json'

division_code = '001'

result = sub_merchant_controller.find_submerchants(
    v_correlation_id,
    chain_code,
    from_created_date,
    to_created_date,
    content_type=content_type,
    division_code=division_code
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


# Find Submerchants VAS

Find submerchants with the Value Added Services they are enrolled for. Date range cannot exceed 90 days between fromCreatedDate and toCreatedDate. A link will be displayed in the results to view additional records. The license key needs to be sent in the request header each time the link is used to view additional records.

```python
def find_submerchants_vas(self,
                         v_correlation_id,
                         chain_code,
                         vas,
                         from_created_date,
                         to_created_date,
                         content_type='application/json',
                         sort_by=None,
                         sort_order=None,
                         limit=None,
                         offset=None,
                         underwriting_status=None,
                         division_code=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The Chain Code a list of submerchants will be returned for |
| `vas` | [`Vas2Enum`](../../doc/models/vas-2-enum.md) | Template, Required | The Value Added Service a submerchant under a specific Chain is enrolled for |
| `from_created_date` | `date` | Query, Required | Filter by when the sub-merchant was created |
| `to_created_date` | `date` | Query, Required | Filter by when the sub-merchant was created |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |
| `sort_by` | [`SortByEnum`](../../doc/models/sort-by-enum.md) | Query, Optional | Sort by certain value |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Sort in ascending or descending order |
| `limit` | `int` | Query, Optional | Limit of Sub-Merchants to respond. Maximum limit is 10. |
| `offset` | `int` | Query, Optional | Row number by which to begin the list (e.g. 10 would start with 10th submerchant) |
| `underwriting_status` | [`UnderwritingStatus1Enum`](../../doc/models/underwriting-status-1-enum.md) | Query, Optional | Look up submerchnats by underwriting status. |
| `division_code` | `str` | Query, Optional | Division Code. Only applicable for PayFacs that are using Divisions. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[SubMerchantsFindVasGetResponse]`](../../doc/models/sub-merchants-find-vas-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

vas = Vas2Enum.REVIEWTRACKERS

from_created_date = dateutil.parser.parse('2016-03-13').date()

to_created_date = dateutil.parser.parse('2016-03-13').date()

content_type = 'application/json'

division_code = '001'

result = sub_merchant_controller.find_submerchants_vas(
    v_correlation_id,
    chain_code,
    vas,
    from_created_date,
    to_created_date,
    content_type=content_type,
    division_code=division_code
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


# Get Submerchant

URI to get information of a PayFac submerchant resource.

```python
def get_submerchant(self,
                   v_correlation_id,
                   id,
                   content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubMerchantsGetResponse`](../../doc/models/sub-merchants-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = sub_merchant_controller.get_submerchant(
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


# Update Submerchant

URI to update information of a PayFac submerchant resource.Please note that all PUT requests are replace requests, and any optional attribute that was provided earlier, but missed in the PUT request will be overridden with NULL.

```python
def update_submerchant(self,
                      v_correlation_id,
                      id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`SubMerchantForUpdate`](../../doc/models/sub-merchant-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = SubMerchantForUpdate(
    dba_name='PayFac Submerchant 01',
    billing_descriptor='PFA*SM',
    business_type=BusinessType1Enum.LODGING,
    business_established_date=dateutil.parser.parse('2016-03-13').date(),
    transaction_type=TransactionTypeEnum.ONLINESTORE,
    website_url='https://payfacsm.com'
)

result = sub_merchant_controller.update_submerchant(
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


# Delete Submerchant

URI to remove a submerchant from the PayFac submerchants collection.

```python
def delete_submerchant(self,
                      v_correlation_id,
                      id,
                      content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = sub_merchant_controller.delete_submerchant(
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
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Patch Submerchant

URI to update all information of a PayFac submerchant resource

```python
def patch_submerchant(self,
                     v_correlation_id,
                     id,
                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`SubMerchantForPatch`](../../doc/models/sub-merchant-for-patch.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubMerchantsGetResponse`](../../doc/models/sub-merchants-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = SubMerchantForPatch(
    dba_name='PayFac Submerchant 01',
    billing_descriptor='PFA*SM',
    mcc_code=7372,
    transaction_type=TransactionTypeEnum.ONLINESTORE,
    division_code='001'
)

result = sub_merchant_controller.patch_submerchant(
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

