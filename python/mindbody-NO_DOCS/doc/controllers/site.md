# Site

```python
site_controller = client.site
```

## Class Name

`SiteController`

## Methods

* [Get Activation Code](../../doc/controllers/site.md#get-activation-code)
* [Get Categories](../../doc/controllers/site.md#get-categories)
* [Get Genders](../../doc/controllers/site.md#get-genders)
* [Get Liability Waiver](../../doc/controllers/site.md#get-liability-waiver)
* [Get Locations](../../doc/controllers/site.md#get-locations)
* [Get Memberships](../../doc/controllers/site.md#get-memberships)
* [Get Mobile Providers](../../doc/controllers/site.md#get-mobile-providers)
* [Get Payment Types](../../doc/controllers/site.md#get-payment-types)
* [Get Programs](../../doc/controllers/site.md#get-programs)
* [Get Promo Codes](../../doc/controllers/site.md#get-promo-codes)
* [Get Prospect Stages](../../doc/controllers/site.md#get-prospect-stages)
* [Get Relationships](../../doc/controllers/site.md#get-relationships)
* [Get Resource Availabilities](../../doc/controllers/site.md#get-resource-availabilities)
* [Get Resources](../../doc/controllers/site.md#get-resources)
* [Get Session Types](../../doc/controllers/site.md#get-session-types)
* [Get Sites](../../doc/controllers/site.md#get-sites)
* [Add Client Index](../../doc/controllers/site.md#add-client-index)
* [Add Promo Code](../../doc/controllers/site.md#add-promo-code)
* [Deactivate Promo Code](../../doc/controllers/site.md#deactivate-promo-code)
* [Update Client Index](../../doc/controllers/site.md#update-client-index)


# Get Activation Code

Before you can use this endpoint, MINDBODY must approve your developer account for live access. If you have finished testing in the sandbox and are ready to begin working with MINDBODY customers, log into your account and request to go live.

See [Accessing Business Data From MINDBODY](https://developers.mindbodyonline.com/PublicDocumentation/V6#accessing-business-data) for more information about the activation code and how to use it.

Once you are approved, this endpoint returns an activation code.This endpoint supports only one site per call.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_activation_code(self,
                       version,
                       authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetActivationCodeResponse`](../../doc/models/get-activation-code-response.md).

## Example Usage

```python
version = '6'

authorization = 'authorization6'

result = site_controller.get_activation_code(
    version,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Categories

Gets the categories.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_categories(self,
                  version,
                  site_id,
                  authorization=None,
                  request_active=None,
                  request_category_ids=None,
                  request_limit=None,
                  request_offset=None,
                  request_service=None,
                  request_sub_category_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active` | `bool` | Query, Optional | When `true`, the response only contains categories which are activated.<br>When `false`, only deactivated categories are returned.<br>Default: **All Categories** |
| `request_category_ids` | `List[int]` | Query, Optional | When included, the response only contains details about the specified category Ids. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_service` | `bool` | Query, Optional | When `true`, the response only contains details about Revenue Categories.<br>When `false`, only Product Revenue Categories are returned.<br>Default: **All Categories** |
| `request_sub_category_ids` | `List[int]` | Query, Optional | When included, the response only contains details about the specified subcategory Ids. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetCategoriesResponse`](../../doc/models/get-categories-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

request_category_ids = [
    140,
    141
]

request_limit = 62

request_offset = 100

request_service = False

request_sub_category_ids = [
    173,
    174,
    175
]

result = site_controller.get_categories(
    version,
    site_id,
    authorization=authorization,
    request_active=request_active,
    request_category_ids=request_category_ids,
    request_limit=request_limit,
    request_offset=request_offset,
    request_service=request_service,
    request_sub_category_ids=request_sub_category_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Genders

The endpoint returns a list of configured client gender options for a site. Custom gender options are assignable to client genders only. Currently, custom values returned from this endpoint cannot be used as input for other endpoints to specify the genders of staff or client preferences.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_genders(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetGendersResponse`](../../doc/models/get-genders-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = site_controller.get_genders(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Liability Waiver

Gets Liability Waiver content at the specified business.
This endpoint requires staff user credentials.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_liability_waiver(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetLiabilityWaiverResponse`](../../doc/models/get-liability-waiver-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = site_controller.get_liability_waiver(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Locations

Get locations for a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_locations(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetLocationsResponse`](../../doc/models/get-locations-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

result = site_controller.get_locations(
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


# Get Memberships

Get the memberships at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_memberships(self,
                   version,
                   site_id,
                   authorization=None,
                   request_membership_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_membership_ids` | `List[int]` | Query, Optional | The requested membership IDs.<br /><br>Default: **all** IDs that the authenticated user’s access level allows. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetMembershipsResponse`](../../doc/models/get-memberships-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_membership_ids = [
    213,
    214
]

result = site_controller.get_memberships(
    version,
    site_id,
    authorization=authorization,
    request_membership_ids=request_membership_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Mobile Providers

Get the list of mobile providers that are supported by the business.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_mobile_providers(self,
                        version,
                        site_id,
                        authorization=None,
                        request_active=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active` | `bool` | Query, Optional | When `true`, the response only contains mobile providers which are activated.<br>When `false`, only deactivated mobile providers are returned.<br>Default: **All Mobile Providers** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetMobileProvidersResponse`](../../doc/models/get-mobile-providers-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

result = site_controller.get_mobile_providers(
    version,
    site_id,
    authorization=authorization,
    request_active=request_active
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Payment Types

Get payment types for a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_payment_types(self,
                     version,
                     site_id,
                     authorization=None,
                     request_active=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active` | `bool` | Query, Optional | When `true`, the response only contains payment types which are activated.<br>When `false`, only deactivated payment types are returned.<br>Default: **All Payment Types** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPaymentTypesResponse`](../../doc/models/get-payment-types-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

result = site_controller.get_payment_types(
    version,
    site_id,
    authorization=authorization,
    request_active=request_active
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Programs

Get service categories offered at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_programs(self,
                version,
                site_id,
                authorization=None,
                request_limit=None,
                request_offset=None,
                request_online_only=None,
                request_program_ids=None,
                request_schedule_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_online_only` | `bool` | Query, Optional | If `true`, filters results to show only those programs that are shown online.<br /><br>If `false`, all programs are returned.<br /><br>Default: **false** |
| `request_program_ids` | `List[int]` | Query, Optional | Program Ids to filter for |
| `request_schedule_type` | [`RequestScheduleTypeEnum`](../../doc/models/request-schedule-type-enum.md) | Query, Optional | A schedule type used to filter the returned results. Possible values are:<br><br>* All<br>* Class<br>* Enrollment<br>* Appointment<br>* Resource<br>* Media<br>* Arrival |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProgramsResponse`](../../doc/models/get-programs-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

request_online_only = False

request_program_ids = [
    91,
    92,
    93
]

request_schedule_type = RequestScheduleTypeEnum.RESOURCE

result = site_controller.get_programs(
    version,
    site_id,
    authorization=authorization,
    request_limit=request_limit,
    request_offset=request_offset,
    request_online_only=request_online_only,
    request_program_ids=request_program_ids,
    request_schedule_type=request_schedule_type
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Promo Codes

Gets a list of promocodes at the specified business. This endpoint requires staff user credentials.
This staff member should have enabled the Set up promotions / **Semester discounts** staff permission.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_promo_codes(self,
                   version,
                   site_id,
                   authorization=None,
                   request_active_only=None,
                   request_end_date=None,
                   request_last_modified_date=None,
                   request_limit=None,
                   request_offset=None,
                   request_online_only=None,
                   request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active_only` | `bool` | Query, Optional | If true, filters results to show only promocodes that are active. If **false**, all promocodes are returned.<br>Default: **true** |
| `request_end_date` | `datetime` | Query, Optional | Filters results to promocodes that were activated before this date. |
| `request_last_modified_date` | `datetime` | Query, Optional | Filters results to promocodes that were modified on or after this date. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_online_only` | `bool` | Query, Optional | If `true`, filters results to show only promocodes that can be used for online sale.<br>If `false`, all promocodes are returned.<br>Default: **false** |
| `request_start_date` | `datetime` | Query, Optional | Filters results to promocodes that were activated after this date. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetPromoCodesResponse`](../../doc/models/get-promo-codes-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active_only = False

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_last_modified_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_online_only = False

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = site_controller.get_promo_codes(
    version,
    site_id,
    authorization=authorization,
    request_active_only=request_active_only,
    request_end_date=request_end_date,
    request_last_modified_date=request_last_modified_date,
    request_limit=request_limit,
    request_offset=request_offset,
    request_online_only=request_online_only,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Prospect Stages

Get the list of prospect stages that represent the prospect stage options for prospective clients.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_prospect_stages(self,
                       version,
                       site_id,
                       authorization=None,
                       request_active=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active` | `bool` | Query, Optional | When `true`, the response only contains prospect stages which are activated.<br>When `false`, only deactivated prospect stages are returned.<br>Default: **All Prospect Stages** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetProspectStagesResponse`](../../doc/models/get-prospect-stages-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

result = site_controller.get_prospect_stages(
    version,
    site_id,
    authorization=authorization,
    request_active=request_active
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Relationships

This endpoint retrieves the business site relationships.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_relationships(self,
                     version,
                     site_id,
                     authorization=None,
                     request_active=None,
                     request_limit=None,
                     request_offset=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active` | `bool` | Query, Optional | When `true`, the response only contains relationships which are activated.<br>When `false`, only deactivated relationships are returned.<br>Default: **All Relationships** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetRelationshipsResponse`](../../doc/models/get-relationships-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

request_limit = 62

request_offset = 100

result = site_controller.get_relationships(
    version,
    site_id,
    authorization=authorization,
    request_active=request_active,
    request_limit=request_limit,
    request_offset=request_offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Resource Availabilities

Get resource availabilities used at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_resource_availabilities(self,
                               version,
                               site_id,
                               authorization=None,
                               request_end_date=None,
                               request_limit=None,
                               request_location_ids=None,
                               request_offset=None,
                               request_program_ids=None,
                               request_resource_ids=None,
                               request_schedule_types=None,
                               request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date` | `datetime` | Query, Optional | End date. If default, StartDate is used. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | Filter by location ids (optional) |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | Filter by program ids (optional) |
| `request_resource_ids` | `List[int]` | Query, Optional | Filter on resourceIds |
| `request_schedule_types` | [`List[RequestScheduleTypeEnum]`](../../doc/models/request-schedule-type-enum.md) | Query, Optional | Filter by schedule types (optional) |
| `request_start_date` | `datetime` | Query, Optional | Start time |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetResourcesResponse`](../../doc/models/get-resources-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_resource_ids = [
    62
]

request_schedule_types = [
    RequestScheduleTypeEnum.APPOINTMENT,
    RequestScheduleTypeEnum.RESOURCE,
    RequestScheduleTypeEnum.MEDIA
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = site_controller.get_resource_availabilities(
    version,
    site_id,
    authorization=authorization,
    request_end_date=request_end_date,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_program_ids=request_program_ids,
    request_resource_ids=request_resource_ids,
    request_schedule_types=request_schedule_types,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Resources

Get resources used at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_resources(self,
                 version,
                 site_id,
                 authorization=None,
                 request_end_date_time=None,
                 request_include_inactive=None,
                 request_limit=None,
                 request_location_id=None,
                 request_location_ids=None,
                 request_offset=None,
                 request_program_ids=None,
                 request_resource_ids=None,
                 request_schedule_types=None,
                 request_session_type_ids=None,
                 request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date_time` | `datetime` | Query, Optional | The time the resource ends. This parameter is ignored if `EndDateTime` or `LocationID` is not set. |
| `request_include_inactive` | `bool` | Query, Optional | Enable to include inactive |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | The location of the resource. This parameter is ignored if `EndDateTime` or `LocationID` is not set.<br /><br>Default: **all** |
| `request_location_ids` | `List[int]` | Query, Optional | Filter by location ids (optional) |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | Filter by program ids (optional) |
| `request_resource_ids` | `List[int]` | Query, Optional | Filter on resourceIds |
| `request_schedule_types` | [`List[RequestScheduleTypeEnum]`](../../doc/models/request-schedule-type-enum.md) | Query, Optional | Filter by schedule types (optional) |
| `request_session_type_ids` | `List[int]` | Query, Optional | List of session type IDs.<br /><br>Default: **all** |
| `request_start_date_time` | `datetime` | Query, Optional | The time the resource starts. This parameter is ignored if `EndDateTime` or `LocationID` is not set. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_include_inactive = False

request_limit = 62

request_location_id = 90

request_location_ids = [
    192
]

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_resource_ids = [
    62
]

request_schedule_types = [
    RequestScheduleTypeEnum.APPOINTMENT,
    RequestScheduleTypeEnum.RESOURCE,
    RequestScheduleTypeEnum.MEDIA
]

request_session_type_ids = [
    228,
    229
]

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = site_controller.get_resources(
    version,
    site_id,
    authorization=authorization,
    request_end_date_time=request_end_date_time,
    request_include_inactive=request_include_inactive,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_program_ids=request_program_ids,
    request_resource_ids=request_resource_ids,
    request_schedule_types=request_schedule_types,
    request_session_type_ids=request_session_type_ids,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Session Types

Get the session types used at a site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_session_types(self,
                     version,
                     site_id,
                     authorization=None,
                     request_limit=None,
                     request_offset=None,
                     request_online_only=None,
                     request_program_i_ds=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_online_only` | `bool` | Query, Optional | When `true`, indicates that only the session types that can be booked online should be returned.<br /><br>Default: **false** |
| `request_program_i_ds` | `List[int]` | Query, Optional | Filters results to session types that belong to one of the given program IDs. If omitted, all program IDs return. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetSessionTypesResponse`](../../doc/models/get-session-types-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

request_online_only = False

request_program_i_ds = [
    52,
    53,
    54
]

result = site_controller.get_session_types(
    version,
    site_id,
    authorization=authorization,
    request_limit=request_limit,
    request_offset=request_offset,
    request_online_only=request_online_only,
    request_program_i_ds=request_program_i_ds
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Sites

Gets a list of sites that the developer has permission to view.

* Passing in no `SiteIds` returns all sites that the developer has access to.
* Passing in one `SiteIds` returns more detailed information about the specified site.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_sites(self,
             version,
             authorization=None,
             request_include_lead_channels=None,
             request_limit=None,
             request_offset=None,
             request_site_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_include_lead_channels` | `bool` | Query, Optional | This is an optional parameter to get lead channels for a Site. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_site_ids` | `List[int]` | Query, Optional | List of the requested site IDs. When omitted, returns all sites that the source has access to. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetSitesResponse`](../../doc/models/get-sites-response.md).

## Example Usage

```python
version = '6'

authorization = 'authorization6'

request_include_lead_channels = False

request_limit = 62

request_offset = 100

request_site_ids = [
    135,
    136
]

result = site_controller.get_sites(
    version,
    authorization=authorization,
    request_include_lead_channels=request_include_lead_channels,
    request_limit=request_limit,
    request_offset=request_offset,
    request_site_ids=request_site_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Client Index

Creates a new client index record at the specified business.
This endpoint requires staff user credentials.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_client_index(self,
                    version,
                    request,
                    site_id,
                    authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddSiteClientIndexRequest`](../../doc/models/add-site-client-index-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddSiteClientIndexResponse`](../../doc/models/add-site-client-index-response.md).

## Example Usage

```python
version = '6'

request = AddSiteClientIndexRequest(
    client_index_name='ClientIndexName2',
    active=False,
    show_on_new_client=False,
    show_on_enrollment_roster=False,
    edit_on_enrollment_roster=False,
    sort_order=50
)

site_id = '-99'

authorization = 'authorization6'

result = site_controller.add_client_index(
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


# Add Promo Code

Creates a new promocode record at the specified business.
This endpoint requires staff user credentials. This staff memeber should have enabled the **Set up promotions / Semester discounts** staff permission.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_promo_code(self,
                  version,
                  request,
                  site_id,
                  authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddPromoCodeRequest`](../../doc/models/add-promo-code-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddPromoCodeResponse`](../../doc/models/add-promo-code-response.md).

## Example Usage

```python
version = '6'

request = AddPromoCodeRequest(
    code='Code6',
    name='Name6',
    active=False,
    discount=Discount(
        mtype='Type6',
        amount=80.68
    ),
    activation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    expiration_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    max_uses=192
)

site_id = '-99'

authorization = 'authorization6'

result = site_controller.add_promo_code(
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


# Deactivate Promo Code

Deactivates an existing promocode record at the specified business.
This endpoint requires staff user credentials. This staff memeber should have enabled the **Set up promotions / Semester discounts** staff permission.

:information_source: **Note** This endpoint does not require authentication.

```python
def deactivate_promo_code(self,
                         version,
                         request,
                         site_id,
                         authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`DeactivatePromoCodeRequest`](../../doc/models/deactivate-promo-code-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
version = '6'

request = DeactivatePromoCodeRequest(
    promotion_id=42
)

site_id = '-99'

authorization = 'authorization6'

result = site_controller.deactivate_promo_code(
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


# Update Client Index

Updates an exisitng client index record at the specified business.
This endpoint requires staff user credentials.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_client_index(self,
                       version,
                       request,
                       site_id,
                       authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateSiteClientIndexRequest`](../../doc/models/update-site-client-index-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateSiteClientIndexResponse`](../../doc/models/update-site-client-index-response.md).

## Example Usage

```python
version = '6'

request = UpdateSiteClientIndexRequest(
    client_index_id=194,
    client_index_name='ClientIndexName2',
    active=False,
    show_on_new_client=False,
    show_on_enrollment_roster=False,
    edit_on_enrollment_roster=False,
    sort_order=50
)

site_id = '-99'

authorization = 'authorization6'

result = site_controller.update_client_index(
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

