# Payroll

```python
payroll_controller = client.payroll
```

## Class Name

`PayrollController`

## Methods

* [Get Commissions](../../doc/controllers/payroll.md#get-commissions)
* [Get Scheduled Service Earnings](../../doc/controllers/payroll.md#get-scheduled-service-earnings)
* [Get Time Cards](../../doc/controllers/payroll.md#get-time-cards)
* [Get Tips](../../doc/controllers/payroll.md#get-tips)


# Get Commissions

A staff authorization token is not required for this endpoint, but if one is passed, its permissions are honored. Depending on the access permissions configured for the staff member whose token is passed,
the endpoint returns either only the payroll information for that staff member or it returns the payroll information for all staff members.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_commissions(self,
                   version,
                   site_id,
                   authorization=None,
                   request_end_date_time=None,
                   request_limit=None,
                   request_location_id=None,
                   request_offset=None,
                   request_staff_id=None,
                   request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date_time` | `datetime` | Query, Optional | The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br /><br>Default: **Today’s date**<br><br>* If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.<br>* If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | A LocationId that you want to retrieve payroll information for. If you do not supply a `LocationId`, data from all locations is returned. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_id` | `int` | Query, Optional | A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. |
| `request_start_date_time` | `datetime` | Query, Optional | The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br><br>* If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.<br>* If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetCommissionsResponse`](../../doc/models/get-commissions-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_staff_id = 180

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = payroll_controller.get_commissions(
    version,
    site_id,
    authorization=authorization,
    request_end_date_time=request_end_date_time,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_staff_id=request_staff_id,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Scheduled Service Earnings

A staff authorization token is not required for this endpoint, but if one is passed, its permissions are honored. Depending on the access permissions configured for the staff member whose token is passed, the endpoint returns either only the payroll information for that staff member or it returns the payroll information for all staff members.

Note that if a staff member is not paid for a class, earnings of zero are returned by this endpoint.

Note that this endpoint calculates both bonus and no-reg rates for assistants.These rates are not supported by the Payroll report in the web interface.

Note that this endpoint returns both the teacher’s adjusted rate and the assistant’s pay rate when the assistant is paid by the teacher.The Payroll report in the web interface only returns the teacher’s adjusted rate.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_scheduled_service_earnings(self,
                                  version,
                                  site_id,
                                  authorization=None,
                                  request_end_date_time=None,
                                  request_limit=None,
                                  request_location_id=None,
                                  request_offset=None,
                                  request_scheduled_service_id=None,
                                  request_scheduled_service_type=None,
                                  request_staff_id=None,
                                  request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date_time` | `datetime` | Query, Optional | The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br /><br>Default: **Today’s date**<br><br>* If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.<br>* If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | A LocationId that you want to retrieve payroll information for. If you do not supply a `LocationId`, data from all locations is returned. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_scheduled_service_id` | `int` | Query, Optional | Filters the results to a single scheduled service. This parameter must be used with a single ScheduledServiceType. |
| `request_scheduled_service_type` | `str` | Query, Optional | Filters the results to schedule service earnings for specific types of services. Possible values:<br><br>* Class<br>* Appointment |
| `request_staff_id` | `int` | Query, Optional | A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. |
| `request_start_date_time` | `datetime` | Query, Optional | The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br><br>* If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.<br>* If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetScheduledServiceEarningsResponse`](../../doc/models/get-scheduled-service-earnings-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_scheduled_service_id = 216

request_scheduled_service_type = 'request.scheduledServiceType6'

request_staff_id = 180

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = payroll_controller.get_scheduled_service_earnings(
    version,
    site_id,
    authorization=authorization,
    request_end_date_time=request_end_date_time,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_scheduled_service_id=request_scheduled_service_id,
    request_scheduled_service_type=request_scheduled_service_type,
    request_staff_id=request_staff_id,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Time Cards

This endpoint returns information for all locations. The **View reports for all locations permission **is not supported for staff auth tokens.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_time_cards(self,
                  version,
                  site_id,
                  authorization=None,
                  request_end_date_time=None,
                  request_limit=None,
                  request_location_id=None,
                  request_offset=None,
                  request_staff_id=None,
                  request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date_time` | `datetime` | Query, Optional | The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br /><br>Default: **Today’s date**<br><br>* If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.<br>* If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | A LocationId that you want to retrieve payroll information for. If you do not supply a `LocationId`, data from all locations is returned. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_id` | `int` | Query, Optional | A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. |
| `request_start_date_time` | `datetime` | Query, Optional | The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br><br>* If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.<br>* If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetTimeCardsResponse`](../../doc/models/get-time-cards-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_staff_id = 180

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = payroll_controller.get_time_cards(
    version,
    site_id,
    authorization=authorization,
    request_end_date_time=request_end_date_time,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_staff_id=request_staff_id,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Tips

A staff authorization token is not required for this endpoint, but if one is passed, its permissions are honored. Depending on the access permissions configured for the staff member whose token is passed,
the endpoint returns either only the payroll information for that staff member or it returns the payroll information for all staff members.
This endpoint returns information for all locations.The** View reports for all locations **permission is not supported for staff auth tokens.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_tips(self,
            version,
            site_id,
            authorization=None,
            request_end_date_time=None,
            request_limit=None,
            request_location_id=None,
            request_offset=None,
            request_staff_id=None,
            request_start_date_time=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `version` | `str` | Template, Required | version of the api. |
| `site_id` | `str` | Header, Required | ID of the site from which to pull data. |
| `authorization` | `str` | Header, Optional | A staff user authorization token. |
| `request_end_date_time` | `datetime` | Query, Optional | The end of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br /><br>Default: **Today’s date**<br><br>* If you do not supply an `EndDateTime`, the data returns for the period from the `StartDateTime` that you supply to today’s date.<br>* If you do not supply an `EndDateTime` or a `StartDateTime`, data returns for the seven days prior to today’s date. |
| `request_limit` | `int` | Query, Optional | Number of results to include, defaults to 100 |
| `request_location_id` | `int` | Query, Optional | A LocationId that you want to retrieve payroll information for. If you do not supply a `LocationId`, data from all locations is returned. |
| `request_offset` | `int` | Query, Optional | Page offset, defaults to 0. |
| `request_staff_id` | `int` | Query, Optional | A list of staff IDs that you want to retrieve payroll information for. If you do not supply a `StaffId`, all active staff members return, ordered by staff ID. |
| `request_start_date_time` | `datetime` | Query, Optional | The beginning of the date range for the payroll information to be returned. The maximum allowed date range is 14 days.<br><br>* If you do not supply a `StartDateTime`, data returns for the seven days prior to the `EndDateTime` that you supply.<br>* If you do not supply either a `StartDateTime` or an `EndDateTime`, the data returns for seven days prior to today’s date. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GetTipsResponse`](../../doc/models/get-tips-response.md).

## Example Usage

```python
version = '6'

site_id = '-99'

authorization = 'authorization6'

request_end_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

request_limit = 62

request_location_id = 90

request_offset = 100

request_staff_id = 180

request_start_date_time = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = payroll_controller.get_tips(
    version,
    site_id,
    authorization=authorization,
    request_end_date_time=request_end_date_time,
    request_limit=request_limit,
    request_location_id=request_location_id,
    request_offset=request_offset,
    request_staff_id=request_staff_id,
    request_start_date_time=request_start_date_time
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

