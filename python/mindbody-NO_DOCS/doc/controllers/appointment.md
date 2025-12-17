# Appointment

```python
appointment_controller = client.appointment
```

## Class Name

`AppointmentController`

## Methods

* [Get Active Session Times](../../doc/controllers/appointment.md#get-active-session-times)
* [Get Add Ons](../../doc/controllers/appointment.md#get-add-ons)
* [Get Appointment Options](../../doc/controllers/appointment.md#get-appointment-options)
* [Get Available Dates](../../doc/controllers/appointment.md#get-available-dates)
* [Get Bookable Items](../../doc/controllers/appointment.md#get-bookable-items)
* [Get Schedule Items](../../doc/controllers/appointment.md#get-schedule-items)
* [Get Staff Appointments](../../doc/controllers/appointment.md#get-staff-appointments)
* [Get Unavailabilities](../../doc/controllers/appointment.md#get-unavailabilities)
* [Add Appointment](../../doc/controllers/appointment.md#add-appointment)
* [Add Appointment Add On](../../doc/controllers/appointment.md#add-appointment-add-on)
* [Update Availability](../../doc/controllers/appointment.md#update-availability)
* [Add Availabilities](../../doc/controllers/appointment.md#add-availabilities)
* [Update Appointment](../../doc/controllers/appointment.md#update-appointment)
* [Remove From Waitlist](../../doc/controllers/appointment.md#remove-from-waitlist)
* [Delete Availability](../../doc/controllers/appointment.md#delete-availability)
* [Delete Appointment Add On](../../doc/controllers/appointment.md#delete-appointment-add-on)


# Get Active Session Times

This is not appointment availability but rather the active business hours for studios and which increments services can be booked at. See BookableItems for appointment availability.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_active_session_times(self,
                            version,
                            site_id,
                            authorization=None,
                            request_end_time=None,
                            request_limit=None,
                            request_offset=None,
                            request_schedule_type=None,
                            request_session_type_ids=None,
                            request_start_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_time` | `datetime` | Query, Optional | Filters results to times that end on or before this time on the current date. Any date provided is ignored..<br><br />Default: **23:59:59** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_schedule_type` | [`RequestScheduleTypeEnum`](../../doc/models/request-schedule-type-enum.md) | Query, Optional | Filters on the provided the schedule type. Either `SessionTypeIds` or `ScheduleType` must be provided. |
| `request_session_type_ids` | `List[int]` | Query, Optional | Filters on the provided session type IDs. Either `SessionTypeIds` or `ScheduleType` must be provided. |
| `request_start_time` | `datetime` | Query, Optional | Filters results to times that start on or after this time on the current date. Any date provided is ignored.<br><br />Default: **00:00:00** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetActiveSessionTimesResponse`](../../doc/models/get-active-session-times-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_schedule_type = RequestScheduleTypeEnum.RESOURCE

request_session_type_ids = [
    228,
    229
]

request_start_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = appointment_controller.get_active_session_times(
    version,
    site_id,
    authorization=authorization,
    request_end_time=request_end_time,
    request_limit=request_limit,
    request_offset=request_offset,
    request_schedule_type=request_schedule_type,
    request_session_type_ids=request_session_type_ids,
    request_start_time=request_start_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Add Ons

Get active appointment add-ons.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_add_ons(self,
               version,
               site_id,
               authorization=None,
               request_limit=None,
               request_offset=None,
               request_staff_id=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_id` | `int` | Query, Optional | Filter to add-ons only performed by this staff member. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetAddOnsResponse`](../../doc/models/get-add-ons-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_limit = 62

request_offset = 100

request_staff_id = 180

result = appointment_controller.get_add_ons(
    version,
    site_id,
    authorization=authorization,
    request_limit=request_limit,
    request_offset=request_offset,
    request_staff_id=request_staff_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Appointment Options

This endpoint has no query parameters.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_appointment_options(self,
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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetAppointmentOptionsResponse`](../../doc/models/get-appointment-options-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.get_appointment_options(
    version,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Available Dates

Returns a list of dates to narrow down staff availability when booking. Dates are those which staff are scheduled to work and do not guarantee booking availabilities. After this call is made, use GET BookableItems to retrieve availabilities for specific dates before booking.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_available_dates(self,
                       version,
                       request_session_type_id,
                       site_id,
                       authorization=None,
                       request_end_date=None,
                       request_location_id=None,
                       request_staff_id=None,
                       request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_session_type_id` | `int` | Query, Required | required requested session type ID. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date` | `datetime` | Query, Optional | The end date of the requested date range.<br><br />Default: **StartDate** |
| `request_location_id` | `int` | Query, Optional | optional requested location ID. |
| `request_staff_id` | `int` | Query, Optional | optional requested staff ID. |
| `request_start_date` | `datetime` | Query, Optional | The start date of the requested date range. If omitted, the default is used.<br><br />Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetAvailableDatesResponse`](../../doc/models/get-available-dates-response.md).

## Example Usage

```python
version = '6'

request_session_type_id = 100

site_id = '-99'

authorization = 'authorization6'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_location_id = 90

request_staff_id = 180

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = appointment_controller.get_available_dates(
    version,
    request_session_type_id,
    site_id,
    authorization=authorization,
    request_end_date=request_end_date,
    request_location_id=request_location_id,
    request_staff_id=request_staff_id,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Bookable Items

Returns a list of availabilities with the information needed to book appointments. Availabilities include information such as the location and its amenities, staff members, programs, and session types. Recommended to use with GET AvailableDates to see what dates the staff is scheduled to work and narrow down the dates searched. Recommended to use with GET ActiveSessionTimes to see which increments each business allows for booking appointments.
Notes:

- With a wider range of dates, this call may take longer to return results.
- With a higher number of request.sessionTypeIds, this call may take longer to return results.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_bookable_items(self,
                      version,
                      request_session_type_ids,
                      site_id,
                      authorization=None,
                      request_appointment_id=None,
                      request_end_date=None,
                      request_ignore_default_session_length=None,
                      request_limit=None,
                      request_location_ids=None,
                      request_offset=None,
                      request_staff_ids=None,
                      request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request_session_type_ids` | `List[int]` | Query, Required | A list of the requested session type IDs. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_appointment_id` | `int` | Query, Optional | If provided, filters out the appointment with this ID. |
| `request_end_date` | `datetime` | Query, Optional | The end date of the requested date range.<br><br />Default: **StartDate** |
| `request_ignore_default_session_length` | `bool` | Query, Optional | When `true`, availabilities that are non-default return, for example, a 30-minute availability with a 60-minute default session length.<br /><br>When `false`, only availabilities that have the default session length return. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | A list of the requested location IDs. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_ids` | `List[int]` | Query, Optional | A list of the requested staff IDs. Omit parameter to return all staff availabilities. |
| `request_start_date` | `datetime` | Query, Optional | The start date of the requested date range.<br><br />Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetBookableItemsResponse`](../../doc/models/get-bookable-items-response.md).

## Example Usage

```python
version = '6'

request_session_type_ids = [
    228,
    229
]

site_id = '-99'

authorization = 'authorization6'

request_appointment_id = 194

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_ignore_default_session_length = False

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = appointment_controller.get_bookable_items(
    version,
    request_session_type_ids,
    site_id,
    authorization=authorization,
    request_appointment_id=request_appointment_id,
    request_end_date=request_end_date,
    request_ignore_default_session_length=request_ignore_default_session_length,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_staff_ids=request_staff_ids,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Schedule Items

Returns a list of schedule items, including appointments, availabilities, and unavailabilities. Unavailabilities are the times at which appointments cannot be booked, for example, on holidays or after hours when the business is closed.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_schedule_items(self,
                      version,
                      site_id,
                      authorization=None,
                      request_end_date=None,
                      request_ignore_prep_finish_times=None,
                      request_limit=None,
                      request_location_ids=None,
                      request_offset=None,
                      request_staff_ids=None,
                      request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date` | `datetime` | Query, Optional | The end date of the requested date range.<br><br />Default: **today’s date** |
| `request_ignore_prep_finish_times` | `bool` | Query, Optional | When `true`, appointment preparation and finish unavailabilities are not returned.<br><br />Default: **false** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | A list of requested location IDs. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_ids` | `List[int]` | Query, Optional | A list of requested staff IDs. |
| `request_start_date` | `datetime` | Query, Optional | The start date of the requested date range.<br><br />Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetScheduleItemsResponse`](../../doc/models/get-schedule-items-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_ignore_prep_finish_times = False

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = appointment_controller.get_schedule_items(
    version,
    site_id,
    authorization=authorization,
    request_end_date=request_end_date,
    request_ignore_prep_finish_times=request_ignore_prep_finish_times,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_staff_ids=request_staff_ids,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Staff Appointments

Returns a list of appointments by staff member.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_staff_appointments(self,
                          version,
                          site_id,
                          authorization=None,
                          request_appointment_ids=None,
                          request_client_id=None,
                          request_end_date=None,
                          request_limit=None,
                          request_location_ids=None,
                          request_offset=None,
                          request_staff_ids=None,
                          request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_appointment_ids` | `List[int]` | Query, Optional | A list of the requested appointment IDs. |
| `request_client_id` | `str` | Query, Optional | The client ID to be returned. |
| `request_end_date` | `datetime` | Query, Optional | The end date of the requested date range.<br><br />Default: **StartDate** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_ids` | `List[int]` | Query, Optional | A list of the requested location IDs. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_ids` | `List[int]` | Query, Optional | List of staff IDs to be returned. Omit parameter to return staff appointments for all staff. |
| `request_start_date` | `datetime` | Query, Optional | The start date of the requested date range. If omitted, the default is used.<br><br />Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetStaffAppointmentsResponse`](../../doc/models/get-staff-appointments-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_appointment_ids = [
    17,
    18
]

request_client_id = 'request.clientId2'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_ids = [
    192
]

request_offset = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = appointment_controller.get_staff_appointments(
    version,
    site_id,
    authorization=authorization,
    request_appointment_ids=request_appointment_ids,
    request_client_id=request_client_id,
    request_end_date=request_end_date,
    request_limit=request_limit,
    request_location_ids=request_location_ids,
    request_offset=request_offset,
    request_staff_ids=request_staff_ids,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Unavailabilities

Returns a list of unavailabilities. Unavailabilities are the times at which appointments cannot be booked, for example, on holidays or after hours when the business is closed.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_unavailabilities(self,
                        version,
                        site_id,
                        authorization=None,
                        request_end_date=None,
                        request_limit=None,
                        request_offset=None,
                        request_staff_ids=None,
                        request_start_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date` | `datetime` | Query, Optional | The end date of the requested date range.<br><br />Default: **today’s date** |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_ids` | `List[int]` | Query, Optional | A list of requested staff IDs. |
| `request_start_date` | `datetime` | Query, Optional | The start date of the requested date range.<br><br />Default: **today’s date** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetUnavailabilitiesResponse`](../../doc/models/get-unavailabilities-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_offset = 100

request_staff_ids = [
    23,
    24,
    25
]

request_start_date = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = appointment_controller.get_unavailabilities(
    version,
    site_id,
    authorization=authorization,
    request_end_date=request_end_date,
    request_limit=request_limit,
    request_offset=request_offset,
    request_staff_ids=request_staff_ids,
    request_start_date=request_start_date
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Appointment

A user token is required for this endpoint. To book an appointment, you must use a location ID, staff ID, client ID, session type ID, and the StartDateTime of the appointment. You can get most of this information using GET BookableItems.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_appointment(self,
                   version,
                   request,
                   site_id,
                   authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddAppointmentRequest`](../../doc/models/add-appointment-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddAppointmentResponse`](../../doc/models/add-appointment-response.md).

## Example Usage

```python
version = '6'

request = AddAppointmentRequest(
    client_id='ClientId0',
    location_id=238,
    session_type_id=82,
    staff_id=188,
    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    apply_payment=False,
    duration=224,
    execute='Execute2',
    end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    gender_preference='GenderPreference6'
)

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.add_appointment(
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


# Add Appointment Add On

This endpoint books an add-on on top of an existing, regular appointment. To book an add-on, you must use an existing appointment ID and session type ID. You can get a session type ID using `GET AppointmentAddOns`.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_appointment_add_on(self,
                          version,
                          request,
                          site_id,
                          authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddAppointmentAddOnRequest`](../../doc/models/add-appointment-add-on-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddAppointmentAddOnResponse`](../../doc/models/add-appointment-add-on-response.md).

## Example Usage

```python
version = '6'

request = AddAppointmentAddOnRequest(
    apply_payment=False,
    appointment_id=246,
    session_type_id=82,
    staff_id=188,
    test=False
)

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.add_appointment_add_on(
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


# Update Availability

To update the information for a specific availability or unavailability of the staff.<br />
Note: You must have a staff user token with the required permissions.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_availability(self,
                       version,
                       site_id,
                       update_availability_request,
                       authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `update_availability_request` | [`UpdateAvailabilityRequest`](../../doc/models/update-availability-request.md) | Body, Required | - |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateAvailabilityResponse`](../../doc/models/update-availability-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

update_availability_request = UpdateAvailabilityRequest(
    availability_ids=[
        12,
        13
    ],
    public_display=PublicDisplayEnum.HIDE,
    days_of_week=[
        DaysOfWeekEnum.SUNDAY,
        DaysOfWeekEnum.MONDAY
    ],
    program_ids=[
        40,
        41
    ],
    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

authorization = 'authorization6'

result = appointment_controller.update_availability(
    version,
    site_id,
    update_availability_request,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Add Availabilities

Add availabilities and unavailabilities for a staff member.<br />
Note: You must have a staff user token with the required permissions.

:information_source: **Note** This endpoint does not require authentication.

```python
def add_availabilities(self,
                      version,
                      request,
                      site_id,
                      authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`AddAvailabilitiesRequest`](../../doc/models/add-availabilities-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AddAvailabilitiesResponse`](../../doc/models/add-availabilities-response.md).

## Example Usage

```python
version = '6'

request = AddAvailabilitiesRequest(
    test=False,
    location_id=38,
    staff_i_ds=[
        125,
        126
    ],
    program_i_ds=[
        144,
        145,
        146
    ],
    start_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.add_availabilities(
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


# Update Appointment

To update the information for a specific appointment, you must have a staff user token with the proper permissions. Note that you can only update the appointment’s `StartDateTime`, `EndDateTime`, `StaffId`, `Notes`, and `SessionTypeId`.

:information_source: **Note** This endpoint does not require authentication.

```python
def update_appointment(self,
                      version,
                      request,
                      site_id,
                      authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `request` | [`UpdateAppointmentRequest`](../../doc/models/update-appointment-request.md) | Body, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UpdateAppointmentResponse`](../../doc/models/update-appointment-response.md).

## Example Usage

```python
version = '6'

request = UpdateAppointmentRequest(
    appointment_id=246,
    end_date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    execute='Execute2',
    gender_preference='GenderPreference6',
    notes='Notes8',
    partner_external_id='PartnerExternalId0'
)

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.update_appointment(
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

Remove an appointment from waitlist

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

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
version = '6'

request_waitlist_entry_ids = [
    138,
    139
]

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.remove_from_waitlist(
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


# Delete Availability

This endpoint deletes the availability or unavailability.
Note: You must have a staff user token with the required permissions.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_availability(self,
                       version,
                       site_id,
                       authorization=None,
                       delete_availability_request_availability_id=None,
                       delete_availability_request_test=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `delete_availability_request_availability_id` | `int` | Query, Optional | The ID of the availability or unavailability. |
| `delete_availability_request_test` | `bool` | Query, Optional | When `true`, indicates that this is a test request and no data is deleted from the subscriber’s database.<br>When `false`, the record will be deleted.<br>Default: **false** |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

delete_availability_request_availability_id = 186

delete_availability_request_test = False

result = appointment_controller.delete_availability(
    version,
    site_id,
    authorization=authorization,
    delete_availability_request_availability_id=delete_availability_request_availability_id,
    delete_availability_request_test=delete_availability_request_test
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Delete Appointment Add On

This endpoint can be used to early-cancel a booked appointment add-on.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_appointment_add_on(self,
                             version,
                             id,
                             site_id,
                             authorization=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `id` | `int` | Query, Required | - |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
version = '6'

id = 112

site_id = '-99'

authorization = 'authorization6'

result = appointment_controller.delete_appointment_add_on(
    version,
    id,
    site_id,
    authorization=authorization
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

