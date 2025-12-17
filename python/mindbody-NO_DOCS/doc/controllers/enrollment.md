# Enrollment

```python
enrollment_controller = client.enrollment
```

## Class Name

`EnrollmentController`

## Methods

* [Get Enrollments](../../doc/controllers/enrollment.md#get-enrollments)
* [Add Client to Enrollment](../../doc/controllers/enrollment.md#add-client-to-enrollment)
* [Add Enrollment Schedule](../../doc/controllers/enrollment.md#add-enrollment-schedule)
* [Update Enrollment Schedule](../../doc/controllers/enrollment.md#update-enrollment-schedule)


# Get Enrollments

Returns a list of enrollments. An enrollment is a service, such as a workshop or an event, that a staff member offers to multiple students, who commit to coming to all or most of the scheduled sessions. Enrollments typically run for a limited time only.

When a user token is not passed with the request or the passed user token has insufficient viewing permissions, only the following staff data is returned in the response:

* FirstName
* LastName
* Id
* Bio
* DisplayName
* ImageUrl

:information_source: **Note** This endpoint does not require authentication.

```python
def get_enrollments(self,
                   version,
                   site_id,
                   authorization=None,
                   request_class_schedule_ids=None,
                   request_end_date=None,
                   request_limit=None,
                   request_location_ids=None,
                   request_offset=None,
                   request_program_ids=None,
                   request_session_type_ids=None,
                   request_staff_ids=None,
                   request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_class_schedule_ids` | `List[int]` | Query, Optional | A list of the requested class schedule IDs. If omitted, all class schedule IDs return. |
| `request_end_date` | `datetime` | Query, Optional | The end of the date range. The response returns any active enrollments that occur on or before this day.<br /><br>Default: **StartDate** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | List of the IDs for the requested locations. If omitted, all location IDs return. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | List of the IDs for the requested programs. If omitted, all program IDs return. |
| `request_session_type_ids` | `List[int]` | Query, Optional | List of the IDs for the requested session types. If omitted, all session types IDs return. |
| `request_staff_ids` | `List[int]` | Query, Optional | List of the IDs for the requested staff IDs. If omitted, all staff IDs return. |
| `request_start_date` | `datetime` | Query, Optional | The start of the date range. The response returns any active enrollments that occur on or after this day.<br /><br>Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetEnrollmentsResponse`](../../doc/models/get-enrollments-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_schedule_ids = [
    149,
    150,
    151
]

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

request_session_type_ids = [
    228,
    229
]

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = enrollment_controller.get_enrollments(
    version,
    site_id,
    authorization=authorization,
    request_class_schedule_ids=request_class_schedule_ids,
    request_end_date=request_end_date,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_program_ids=request_program_ids,
    request_session_type_ids=request_session_type_ids,
    request_staff_ids=request_staff_ids,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Client to Enrollment

Book a client into an enrollment.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_client_to_enrollment(self,
                            version,
                            request,
                            site_id,
                            authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddClientToEnrollmentRequest`](../../doc/models/add-client-to-enrollment-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ClassSchedule`](../../doc/models/class-schedule.md).

## Example Usage

```python
version = '6'

request = AddClientToEnrollmentRequest(
    client_id='ClientId0',
    class_schedule_id=36,
    enroll_date_forward=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    enroll_open=[
        dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    ],
    test=False,
    send_email=False,
    waitlist=False
)

site_id = '-99'

authorization = 'authorization6'

result = enrollment_controller.add_client_to_enrollment(
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


# Add Enrollment Schedule

This endpoint adds a enrollment schedule. You can require clients to sign up for the entire enrollment schedule or allow them to pick specific sessions using the AllowOpenEnrollment parameter.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_enrollment_schedule(self,
                           version,
                           request,
                           site_id,
                           authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddClassEnrollmentScheduleRequest`](../../doc/models/add-class-enrollment-schedule-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WrittenClassSchedulesInfo`](../../doc/models/written-class-schedules-info.md).

## Example Usage

```python
version = '6'

request = AddClassEnrollmentScheduleRequest(
    class_description_id=66,
    location_id=238,
    start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    start_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

site_id = '-99'

authorization = 'authorization6'

result = enrollment_controller.add_enrollment_schedule(
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


# Update Enrollment Schedule

This endpoint update a enrollment schedule.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_enrollment_schedule(self,
                              version,
                              request,
                              site_id,
                              authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateClassEnrollmentScheduleRequest`](../../doc/models/update-class-enrollment-schedule-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WrittenClassSchedulesInfo`](../../doc/models/written-class-schedules-info.md).

## Example Usage

```python
version = '6'

request = UpdateClassEnrollmentScheduleRequest(
    class_id=90,
    class_description_id=66,
    location_id=238,
    start_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    end_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

site_id = '-99'

authorization = 'authorization6'

result = enrollment_controller.update_enrollment_schedule(
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

