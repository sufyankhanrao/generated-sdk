# Staff

```python
staff_controller = client.staff
```

## Class Name

`StaffController`

## Methods

* [Get Staff Image URL](../../doc/controllers/staff.md#get-staff-image-url)
* [Get Sales Reps](../../doc/controllers/staff.md#get-sales-reps)
* [Get Staff Session Types](../../doc/controllers/staff.md#get-staff-session-types)
* [Get Staff](../../doc/controllers/staff.md#get-staff)
* [Get Staff Permissions](../../doc/controllers/staff.md#get-staff-permissions)
* [Add Staff](../../doc/controllers/staff.md#add-staff)
* [Assign Staff Session Type](../../doc/controllers/staff.md#assign-staff-session-type)
* [Add Staff Availability](../../doc/controllers/staff.md#add-staff-availability)
* [Update Staff](../../doc/controllers/staff.md#update-staff)
* [Update Staff Permissions](../../doc/controllers/staff.md#update-staff-permissions)


# Get Staff Image URL

This endpoint can be utilized to retrieve image urls for requested staff member.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_staff_image_url(self,
                       version,
                       site_id,
                       authorization=None,
                       request_staff_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_staff_id` | `int` | Query, Optional | The ID of the staff member whose image URL details you want to retrieve. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetStaffImageURLResponse`](../../doc/models/get-staff-image-url-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_staff_id = 180

result = staff_controller.get_staff_image_url(
    version,
    site_id,
    authorization=authorization,
    request_staff_id=request_staff_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Sales Reps

This endpoint returns the basic details of the staffs that are marked as sales reps.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_sales_reps(self,
                  version,
                  site_id,
                  authorization=None,
                  request_active_only=None,
                  request_limit=None,
                  request_offset=None,
                  request_sales_rep_numbers=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active_only` | `bool` | Query, Optional | When `true`, will return only active reps data.<br>Default : **false** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_sales_rep_numbers` | `List[int]` | Query, Optional | This is the list of the sales rep numbers for which the salesrep data will be fetched. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetSalesRepsResponse`](../../doc/models/get-sales-reps-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active_only = False

request_limit = 62

request_offset = 100

request_sales_rep_numbers = [
    123,
    124,
    125
]

result = staff_controller.get_sales_reps(
    version,
    site_id,
    authorization=authorization,
    request_active_only=request_active_only,
    request_limit=request_limit,
    request_offset=request_offset,
    request_sales_rep_numbers=request_sales_rep_numbers
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Staff Session Types

Gets a list of active session types for a specific staff member. A staff user token must be included with staff assigned the ManageStaffPayRates permission.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_staff_session_types(self,
                           version,
                           request_staff_id,
                           site_id,
                           authorization=None,
                           request_limit=None,
                           request_offset=None,
                           request_online_only=None,
                           request_program_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_staff_id` | `int` | Query, Required | The ID of the staff member whose session types you want to return. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_online_only` | `bool` | Query, Optional | When `true`, indicates that only the session types that can be booked online should be returned.<br>Default: **false** |
| `request_program_ids` | `List[int]` | Query, Optional | Filters results to session types that belong to one of the given program IDs. If omitted, all program IDs return. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetStaffSessionTypesResponse`](../../doc/models/get-staff-session-types-response.md).

## Example Usage

```python
version = '6'

request_staff_id = 180

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

result = staff_controller.get_staff_session_types(
    version,
    request_staff_id,
    site_id,
    authorization=authorization,
    request_limit=request_limit,
    request_offset=request_offset,
    request_online_only=request_online_only,
    request_program_ids=request_program_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Staff

When a user token is not passed with the request or the passed user token has insufficient viewing permissions, only the following staff data is returned in the response:

* FirstName
* LastName
* Id
* Bio
* DisplayName
* ImageUrl
* EmpID

:information_source: **Note** This endpoint does not require authentication.

```python
def get_staff(self,
             version,
             site_id,
             authorization=None,
             request_filters=None,
             request_limit=None,
             request_location_id=None,
             request_offset=None,
             request_session_type_id=None,
             request_staff_ids=None,
             request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_filters` | `List[str]` | Query, Optional | Filters to apply to the search. Possible values are:<br><br>* StaffViewable<br>* AppointmentInstructor<br>* ClassInstructor<br>* Male<br>* Female |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | Return only staff members that are available at the specified location. You must supply a valid `SessionTypeID` and `StartDateTime` to use this parameter. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_session_type_id` | `int` | Query, Optional | Return only staff members that are available for the specified session type. You must supply a valid `StartDateTime` and `LocationID` to use this parameter. |
| `request_staff_ids` | `List[int]` | Query, Optional | A list of the requested staff IDs. |
| `request_start_date_time` | `datetime` | Query, Optional | Return only staff members that are available at the specified date and time. You must supply a valid `SessionTypeID` and `LocationID` to use this parameter. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetStaffResponse`](../../doc/models/get-staff-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_filters = [
    'request.filters0',
    'request.filters1',
    'request.filters2'
]

request_limit = 62

request_location_id = 90

request_offset = 100

request_session_type_id = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = staff_controller.get_staff(
    version,
    site_id,
    authorization=authorization,
    request_filters=request_filters,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_session_type_id=request_session_type_id,
    request_staff_ids=request_staff_ids,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Staff Permissions

Get configured staff permissions for a staff member.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_staff_permissions(self,
                         version,
                         request_staff_id,
                         site_id,
                         authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_staff_id` | `int` | Query, Required | The ID of the staff member whose permissions you want to return. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetStaffPermissionsResponse`](../../doc/models/get-staff-permissions-response.md).

## Example Usage

```python
version = '6'

request_staff_id = 180

site_id = '-99'

authorization = 'authorization6'

result = staff_controller.get_staff_permissions(
    version,
    request_staff_id,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Staff

Creates a new staff member record at the specified business. The `FirstName` and `LastName` parameters are always required for this request.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_staff(self,
             version,
             request,
             site_id,
             authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddStaffRequest`](../../doc/models/add-staff-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddStaffResponse`](../../doc/models/add-staff-response.md).

## Example Usage

```python
version = '6'

request = AddStaffRequest(
    first_name='FirstName8',
    last_name='LastName8',
    email='Email8',
    is_male=False,
    home_phone='HomePhone8',
    work_phone='WorkPhone2',
    mobile_phone='MobilePhone6'
)

site_id = '-99'

authorization = 'authorization6'

result = staff_controller.add_staff(
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


# Assign Staff Session Type

Assigns a staff member to an appointment session type with staff specific properties such as time length and pay rate. A staff user token must be included with staff assigned the ManageStaffPayRates permission.

:information_source: **Note** This endpoint does not require authentication.

```python
def assign_staff_session_type(self,
                             version,
                             request,
                             site_id,
                             authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AssignStaffSessionTypeRequest`](../../doc/models/assign-staff-session-type-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AssignStaffSessionTypeResponse`](../../doc/models/assign-staff-session-type-response.md).

## Example Usage

```python
version = '6'

request = AssignStaffSessionTypeRequest(
    staff_id=188,
    session_type_id=82,
    active=False,
    time_length=222,
    prep_time=166,
    finish_time=246,
    pay_rate_type='PayRateType2',
    pay_rate_amount=169.62
)

site_id = '-99'

authorization = 'authorization6'

result = staff_controller.assign_staff_session_type(
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


# Add Staff Availability

Enables to add staff availability or unavailability for a given staff member.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_staff_availability(self,
                          version,
                          request,
                          site_id,
                          authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddStaffAvailabilityRequest`](../../doc/models/add-staff-availability-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
version = '6'

request = AddStaffAvailabilityRequest(
    staff_id=188,
    is_availability=False,
    days_of_week=[
        'DaysOfWeek7'
    ],
    start_time='StartTime4',
    end_time='EndTime0',
    start_date='StartDate0',
    end_date='EndDate6',
    description='Description0',
    program_ids=[
        238
    ],
    location_id=238,
    status='Status4'
)

site_id = '-99'

authorization = 'authorization6'

result = staff_controller.add_staff_availability(
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


# Update Staff

Updates an existing staff member record at the specified business. The ID is a required parameters for this request.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_staff(self,
                version,
                request,
                site_id,
                authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateStaffRequest`](../../doc/models/update-staff-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateStaffResponse`](../../doc/models/update-staff-response.md).

## Example Usage

```python
version = '6'

request = UpdateStaffRequest(
    id=142,
    first_name='FirstName8',
    last_name='LastName8',
    email='Email8',
    is_male=False,
    home_phone='HomePhone8'
)

site_id = '-99'

authorization = 'authorization6'

result = staff_controller.update_staff(
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


# Update Staff Permissions

Assigns a permission group to a staff member. A staff user token must be included with staff assigned the ManageStaffPayRates permission.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_staff_permissions(self,
                            version,
                            request,
                            site_id,
                            authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateStaffPermissionsRequest`](../../doc/models/update-staff-permissions-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateStaffPermissionsResponse`](../../doc/models/update-staff-permissions-response.md).

## Example Usage

```python
version = '6'

request = UpdateStaffPermissionsRequest(
    staff_id=188,
    permission_group_name='PermissionGroupName8'
)

site_id = '-99'

authorization = 'authorization6'

result = staff_controller.update_staff_permissions(
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

