# Class

```python
mclass_controller = client.mclass
```

## Class Name

`ClassController`

## Methods

* [Get Class Descriptions](../../doc/controllers/class.md#get-class-descriptions)
* [Get Classes](../../doc/controllers/class.md#get-classes)
* [Get Class Schedules](../../doc/controllers/class.md#get-class-schedules)
* [Get Class Visits](../../doc/controllers/class.md#get-class-visits)
* [Get Courses](../../doc/controllers/class.md#get-courses)
* [Get Semesters](../../doc/controllers/class.md#get-semesters)
* [Get Waitlist Entries](../../doc/controllers/class.md#get-waitlist-entries)
* [Add Class Schedule](../../doc/controllers/class.md#add-class-schedule)
* [Add Client to Class](../../doc/controllers/class.md#add-client-to-class)
* [Cancel Single Class](../../doc/controllers/class.md#cancel-single-class)
* [Remove Client From Class](../../doc/controllers/class.md#remove-client-from-class)
* [Remove Clients From Classes](../../doc/controllers/class.md#remove-clients-from-classes)
* [Remove From Waitlist](../../doc/controllers/class.md#remove-from-waitlist)
* [Substitute Class Teacher](../../doc/controllers/class.md#substitute-class-teacher)
* [Update Class Schedule](../../doc/controllers/class.md#update-class-schedule)


# Get Class Descriptions

To find class descriptions associated with **scheduled classes**, pass `StaffId`, `StartClassDateTime`, `EndClassDateTime`, or `LocationId` in the request.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_class_descriptions(self,
                          version,
                          site_id,
                          authorization=None,
                          request_class_description_id=None,
                          request_end_class_date_time=None,
                          request_limit=None,
                          request_location_id=None,
                          request_offset=None,
                          request_program_ids=None,
                          request_staff_id=None,
                          request_start_class_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_class_description_id` | `int` | Query, Optional | The ID of the requested client. |
| `request_end_class_date_time` | `datetime` | Query, Optional | Filters the results to class descriptions for scheduled classes that happen before the given date and time. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | Filters results to classes descriptions for schedule classes as the given location. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | A list of requested program IDs. |
| `request_staff_id` | `int` | Query, Optional | Filters results to class descriptions for scheduled classes taught by the given staff member. |
| `request_start_class_date_time` | `datetime` | Query, Optional | Filters the results to class descriptions for scheduled classes that happen on or after the given date and time. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetClassDescriptionsResponse`](../../doc/models/get-class-descriptions-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_description_id = 62

request_end_class_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_program_ids = [
    91,
    92,
    93
]

request_staff_id = 180

request_start_class_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = mclass_controller.get_class_descriptions(
    version,
    site_id,
    authorization=authorization,
    request_class_description_id=request_class_description_id,
    request_end_class_date_time=request_end_class_date_time,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_program_ids=request_program_ids,
    request_staff_id=request_staff_id,
    request_start_class_date_time=request_start_class_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Classes

Get scheduled classes.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_classes(self,
               version,
               site_id,
               authorization=None,
               request_class_description_ids=None,
               request_class_ids=None,
               request_class_schedule_ids=None,
               request_client_id=None,
               request_end_date_time=None,
               request_hide_canceled_classes=None,
               request_last_modified_date=None,
               request_limit=None,
               request_location_ids=None,
               request_offset=None,
               request_program_ids=None,
               request_scheduling_window=None,
               request_semester_ids=None,
               request_session_type_ids=None,
               request_staff_ids=None,
               request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_class_description_ids` | `List[int]` | Query, Optional | The requested class description IDs. |
| `request_class_ids` | `List[int]` | Query, Optional | The requested class IDs. |
| `request_class_schedule_ids` | `List[int]` | Query, Optional | The requested classSchedule Ids. |
| `request_client_id` | `str` | Query, Optional | The client ID of the client who is viewing this class list. Based on identity, the client may be able to see additional information, such as membership specials. |
| `request_end_date_time` | `datetime` | Query, Optional | The requested end date for filtering.<br><br />Default: **today’s date** |
| `request_hide_canceled_classes` | `bool` | Query, Optional | When `true`, canceled classes are removed from the response.<br /><br>When `false`, canceled classes are included in the response.<br /><br>Default: **false** |
| `request_last_modified_date` | `datetime` | Query, Optional | When included in the request, only records modified on or after the `LastModifiedDate` specified are included in the response. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | A list of location IDs on which to base the search. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | A list of program IDs on which to base the search. |
| `request_scheduling_window` | `bool` | Query, Optional | When `true`, classes outside scheduling window are removed from the response.<br /><br>When `false`, classes are included in the response, regardless of the scheduling window.<br /><br>Default: **false** |
| `request_semester_ids` | `List[int]` | Query, Optional | A list of semester IDs on which to base the search. |
| `request_session_type_ids` | `List[int]` | Query, Optional | A list of session type IDs on which to base the search. |
| `request_staff_ids` | `List[int]` | Query, Optional | The requested IDs of the teaching staff members. |
| `request_start_date_time` | `datetime` | Query, Optional | The requested start date for filtering. This also determines what you will see for the ‘BookingWindow’ StartDateTime in the response. For example, if you pass a StartDateTime that is on OR before the BookingWindow ‘Open’ days of the class, you will retrieve the actual ‘StartDateTime’ for the Booking Window. If you pass a StartDateTime that is after the BookingWindow ‘date’, then you will receive results based on that start date. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetClassesResponse`](../../doc/models/get-classes-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_description_ids = [
    107,
    108
]

request_class_ids = [
    87,
    88,
    89
]

request_class_schedule_ids = [
    149,
    150,
    151
]

request_client_id = 'request.clientId2'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_hide_canceled_classes = False

request_last_modified_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

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

request_scheduling_window = False

request_semester_ids = [
    251,
    252
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

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = mclass_controller.get_classes(
    version,
    site_id,
    authorization=authorization,
    request_class_description_ids=request_class_description_ids,
    request_class_ids=request_class_ids,
    request_class_schedule_ids=request_class_schedule_ids,
    request_client_id=request_client_id,
    request_end_date_time=request_end_date_time,
    request_hide_canceled_classes=request_hide_canceled_classes,
    request_last_modified_date=request_last_modified_date,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_program_ids=request_program_ids,
    request_scheduling_window=request_scheduling_window,
    request_semester_ids=request_semester_ids,
    request_session_type_ids=request_session_type_ids,
    request_staff_ids=request_staff_ids,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Class Schedules

Get class schedules.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_class_schedules(self,
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
| `request_class_schedule_ids` | `List[int]` | Query, Optional | The class schedule IDs.<br><br />Default: **all** |
| `request_end_date` | `datetime` | Query, Optional | The end date of the range. Return any active enrollments that occur on or before this day.<br><br />Default: **StartDate** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | The location IDs.<br><br />Default: **all** |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_program_ids` | `List[int]` | Query, Optional | The program IDs.<br><br />Default: **all** |
| `request_session_type_ids` | `List[int]` | Query, Optional | The session type IDs.<br><br />Default: **all** |
| `request_staff_ids` | `List[int]` | Query, Optional | The staff IDs.<br><br />Default: **all** |
| `request_start_date` | `datetime` | Query, Optional | The start date of the range. Return any active enrollments that occur on or after this day.<br><br />Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetClassSchedulesResponse`](../../doc/models/get-class-schedules-response.md).

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

result = mclass_controller.get_class_schedules(
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


# Get Class Visits

Returns a list of visits that contain information for a specified class. On success, this request returns the class object in the response with a list of visits.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_class_visits(self,
                    version,
                    request_class_id,
                    site_id,
                    authorization=None,
                    request_last_modified_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_class_id` | `int` | Query, Required | The class ID. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_last_modified_date` | `datetime` | Query, Optional | When included in the request, only records modified on or after the `LastModifiedDate` specified are included in the response. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetClassVisitsResponse`](../../doc/models/get-class-visits-response.md).

## Example Usage

```python
version = '6'

request_class_id = 222

site_id = '-99'

authorization = 'authorization6'

request_last_modified_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = mclass_controller.get_class_visits(
    version,
    request_class_id,
    site_id,
    authorization=authorization,
    request_last_modified_date=request_last_modified_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Courses

This endpoint will provide all the data related to courses depending on the access level.<br />
Note: The Authorization is an optional header.If Authorization header is not passed, the response will be masked else full response will be provided.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_courses(self,
               version,
               site_id,
               authorization=None,
               get_courses_request_course_i_ds=None,
               get_courses_request_end_date=None,
               get_courses_request_limit=None,
               get_courses_request_location_i_ds=None,
               get_courses_request_offset=None,
               get_courses_request_program_i_ds=None,
               get_courses_request_semester_i_ds=None,
               get_courses_request_staff_i_ds=None,
               get_courses_request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `get_courses_request_course_i_ds` | `List[int]` | Query, Optional | Return only courses that are available for the specified CourseIds. |
| `get_courses_request_end_date` | `datetime` | Query, Optional | The end date range. Any active courses that are on or before this day.<br><br />(optional) Defaults to StartDate. |
| `get_courses_request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `get_courses_request_location_i_ds` | `List[int]` | Query, Optional | Return only courses that are available for the specified LocationIds. |
| `get_courses_request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `get_courses_request_program_i_ds` | `List[int]` | Query, Optional | Return only courses that are available for the specified ProgramIds. |
| `get_courses_request_semester_i_ds` | `List[int]` | Query, Optional | Return only courses that are available for the specified SemesterIds. |
| `get_courses_request_staff_i_ds` | `List[int]` | Query, Optional | Return only courses that are available for the specified StaffIds. |
| `get_courses_request_start_date` | `datetime` | Query, Optional | The start date range. Any active courses that are on or after this day.<br><br />(optional) Defaults to today. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetCoursesReponse`](../../doc/models/get-courses-reponse.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

get_courses_request_course_i_ds = [
    11,
    12,
    13
]

get_courses_request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

get_courses_request_limit = 158

get_courses_request_location_i_ds = [
    175,
    176
]

get_courses_request_offset = 92

get_courses_request_program_i_ds = [
    250
]

get_courses_request_semester_i_ds = [
    73,
    74,
    75
]

get_courses_request_staff_i_ds = [
    73
]

get_courses_request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = mclass_controller.get_courses(
    version,
    site_id,
    authorization=authorization,
    get_courses_request_course_i_ds=get_courses_request_course_i_ds,
    get_courses_request_end_date=get_courses_request_end_date,
    get_courses_request_limit=get_courses_request_limit,
    get_courses_request_location_i_ds=get_courses_request_location_i_ds,
    get_courses_request_offset=get_courses_request_offset,
    get_courses_request_program_i_ds=get_courses_request_program_i_ds,
    get_courses_request_semester_i_ds=get_courses_request_semester_i_ds,
    get_courses_request_staff_i_ds=get_courses_request_staff_i_ds,
    get_courses_request_start_date=get_courses_request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Semesters

This endpoint retrieves the business class semesters.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_semesters(self,
                 version,
                 site_id,
                 authorization=None,
                 request_active=None,
                 request_end_date=None,
                 request_limit=None,
                 request_offset=None,
                 request_semester_i_ds=None,
                 request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_active` | `bool` | Query, Optional | When true, the response only contains semesters which are activated. When false, only deactivated semesters are returned.<br>Default: **All semesters** |
| `request_end_date` | `datetime` | Query, Optional | The end date for the range. All semesters that are on or before this day.<br>Default: **StartDate** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_semester_i_ds` | `List[int]` | Query, Optional | The requested semester IDs. |
| `request_start_date` | `datetime` | Query, Optional | The start date for the range. All semesters that are on or after this day.<br>Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetSemestersResponse`](../../doc/models/get-semesters-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_active = False

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_semester_i_ds = [
    126
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = mclass_controller.get_semesters(
    version,
    site_id,
    authorization=authorization,
    request_active=request_active,
    request_end_date=request_end_date,
    request_limit=request_limit,
    request_offset=request_offset,
    request_semester_i_ds=request_semester_i_ds,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Waitlist Entries

Returns a list of waiting list entries for a specified class schedule or class. The request requires staff credentials and either a class schedule ID or class ID.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_waitlist_entries(self,
                        version,
                        site_id,
                        authorization=None,
                        request_class_ids=None,
                        request_class_schedule_ids=None,
                        request_client_ids=None,
                        request_hide_past_entries=None,
                        request_limit=None,
                        request_offset=None,
                        request_waitlist_entry_ids=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_class_ids` | `List[int]` | Query, Optional | The requested class IDs. If a class ID is present, the request automatically disregards any class schedule IDs in the request. <br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all ClassIds** |
| `request_class_schedule_ids` | `List[int]` | Query, Optional | The requested class schedule IDs. If a class ID is present, the request automatically disregards any class schedule IDs in the request.<br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all ClassScheduleIds** |
| `request_client_ids` | `List[str]` | Query, Optional | The requested client IDs.<br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all ClientIds** |
| `request_hide_past_entries` | `bool` | Query, Optional | When `true`, indicates that past waiting list entries are hidden from clients.<br /><br>When `false`, indicates that past entries are not hidden from clients.<br /><br>Default: **false** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_waitlist_entry_ids` | `List[int]` | Query, Optional | The requested waiting list entry IDs.<br /><br>Either `ClassScheduleIds`, `ClientIds`, `WaitlistEntryIds`, or `ClassIds` is required; the others become optional.<br /><br>Default: **all WaitlistEntryIds** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetWaitlistEntriesResponse`](../../doc/models/get-waitlist-entries-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_class_ids = [
    87,
    88,
    89
]

request_class_schedule_ids = [
    149,
    150,
    151
]

request_client_ids = [
    'request.clientIds9',
    'request.clientIds0',
    'request.clientIds1'
]

request_hide_past_entries = False

request_limit = 62

request_offset = 100

request_waitlist_entry_ids = [
    138,
    139
]

result = mclass_controller.get_waitlist_entries(
    version,
    site_id,
    authorization=authorization,
    request_class_ids=request_class_ids,
    request_class_schedule_ids=request_class_schedule_ids,
    request_client_ids=request_client_ids,
    request_hide_past_entries=request_hide_past_entries,
    request_limit=request_limit,
    request_offset=request_offset,
    request_waitlist_entry_ids=request_waitlist_entry_ids
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Class Schedule

This endpoint adds a class schedule. For a single day schedule, the EndDate parameter can be omitted.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_class_schedule(self,
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

result = mclass_controller.add_class_schedule(
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


# Add Client to Class

This endpoint adds a client to a class or to a class waiting list. To prevent overbooking a class or booking outside the schedule windows set forth by the business, it is necessary to first check the capacity level of the class (‘MaxCapacity’ and 'TotalBooked’) and the 'IsAvailable’ parameter by running the GetClasses REQUEST. It is helpful to use this endpoint in the following situations:

* Use after calling `GET Clients` and `GET Classes` so that you are sure which client to book in which class.
* If adding a client to a class from a waiting list, use this call after you call `GET WaitlistEntries` and determine the ID of the waiting list from which you are moving the client.
* If adding a client to a class and using a pricing option that the client has already purchased, use this call after you call `GET ClientServices` to determine the ID of the pricing option that the client wants to use.

If you add a client to a class and the client purchases a new pricing option, use `GET Services`, `GET Classes`, and then `POST CheckoutShoppingCart` in place of this call.

This endpoint also supports cross-regional class bookings. If you want to perform a cross-regional class booking, set `CrossRegionalBooking` to `true`. This endpoint does not support adding a user to a waiting list using a cross-regional client pricing option(service). Cross-regional booking workflows do not support client service scheduling restrictions.

When performing a cross-regional class booking, this endpoint loops through the first ten sites that the client is associated with, looks for client pricing options at each of those sites, and then uses the oldest client pricing option found.It is important to note that this endpoint only loops through a maximum of ten associated client sites. If a `ClientID` is associated with more than ten sites in an organization, this endpoint only loops through the first ten.If you know that a client has a client service at another site, you can specify that site using the `CrossRegionalBookingClientServiceSiteId` query parameter.

If you perform a cross-regional booking, two additional fields are included in the `SessionType` object of the response:

* `SiteID`, which specifies where the client service is coming from
* `CrossRegionalBookingPerformed`, a Boolean field that is set to `true`

As a prerequisite to using this endpoint, your `SourceName` must have been granted access to the organization to which the site belongs.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_client_to_class(self,
                       version,
                       request,
                       site_id,
                       authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddClientToClassRequest`](../../doc/models/add-client-to-class-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddClientToClassResponse`](../../doc/models/add-client-to-class-response.md).

## Example Usage

```python
version = '6'

request = AddClientToClassRequest(
    client_id='ClientId0',
    class_id=90,
    test=False,
    require_payment=False,
    waitlist=False,
    send_email=False,
    waitlist_entry_id=54
)

site_id = '-99'

authorization = 'authorization6'

result = mclass_controller.add_client_to_class(
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


# Cancel Single Class

This endpoint will cancel a single class from studio.

:information_source: **Note** This endpoint does not require authentication.

```python
def cancel_single_class(self,
                       version,
                       request,
                       site_id,
                       authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`CancelSingleClassRequest`](../../doc/models/cancel-single-class-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CancelSingleClassResponse`](../../doc/models/cancel-single-class-response.md).

## Example Usage

```python
version = '6'

request = CancelSingleClassRequest(
    class_id=30,
    hide_cancel=False,
    send_client_email=False,
    send_staff_email=False
)

site_id = '-99'

authorization = 'authorization6'

result = mclass_controller.cancel_single_class(
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


# Remove Client From Class

Remove a client from a class.

:information_source: **Note** This endpoint does not require authentication.

```python
def remove_client_from_class(self,
                            version,
                            request,
                            site_id,
                            authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`RemoveClientFromClassRequest`](../../doc/models/remove-client-from-class-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RemoveClientFromClassResponse`](../../doc/models/remove-client-from-class-response.md).

## Example Usage

```python
version = '6'

request = RemoveClientFromClassRequest(
    client_id='ClientId0',
    class_id=90,
    test=False,
    send_email=False,
    late_cancel=False,
    visit_id=92
)

site_id = '-99'

authorization = 'authorization6'

result = mclass_controller.remove_client_from_class(
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


# Remove Clients From Classes

This endpoint can be utilized for removing multiple clients from multiple classes in one request.

:information_source: **Note** This endpoint does not require authentication.

```python
def remove_clients_from_classes(self,
                               version,
                               request,
                               site_id,
                               authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`RemoveClientsFromClassesRequest`](../../doc/models/remove-clients-from-classes-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`RemoveClientsFromClassesResponse`](../../doc/models/remove-clients-from-classes-response.md).

## Example Usage

```python
version = '6'

request = RemoveClientsFromClassesRequest(
    details=[
        ClassClientDetail(
            client_ids=[
                'ClientIds5'
            ],
            class_id=190
        ),
        ClassClientDetail(
            client_ids=[
                'ClientIds5'
            ],
            class_id=190
        )
    ],
    test=False,
    send_email=False,
    late_cancel=False,
    limit=32
)

site_id = '-99'

authorization = 'authorization6'

result = mclass_controller.remove_clients_from_classes(
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


# Remove From Waitlist

This endpoint does not return a response. If a call to this endpoint results in a 200 OK HTTP status code, then the call was successful.

:information_source: **Note** This endpoint does not require authentication.

```python
def remove_from_waitlist(self,
                        version,
                        request_waitlist_entry_ids,
                        site_id,
                        authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_waitlist_entry_ids` | `List[int]` | Query, Required | A list of `WaitlistEntryIds` to remove from the waiting list. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
version = '6'

request_waitlist_entry_ids = [
    138,
    139
]

site_id = '-99'

authorization = 'authorization6'

result = mclass_controller.remove_from_waitlist(
    version,
    request_waitlist_entry_ids,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Substitute Class Teacher

Substitute a class teacher.

:information_source: **Note** This endpoint does not require authentication.

```python
def substitute_class_teacher(self,
                            version,
                            request,
                            site_id,
                            authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`SubstituteClassTeacherRequest`](../../doc/models/substitute-class-teacher-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SubstituteClassTeacherResponse`](../../doc/models/substitute-class-teacher-response.md).

## Example Usage

```python
version = '6'

request = SubstituteClassTeacherRequest(
    class_id=90,
    staff_id=188,
    override_conflicts=False,
    send_client_email=False,
    send_original_teacher_email=False,
    send_substitute_teacher_email=False
)

site_id = '-99'

authorization = 'authorization6'

result = mclass_controller.substitute_class_teacher(
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


# Update Class Schedule

This endpoint updates a class schedule.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_class_schedule(self,
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

result = mclass_controller.update_class_schedule(
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

