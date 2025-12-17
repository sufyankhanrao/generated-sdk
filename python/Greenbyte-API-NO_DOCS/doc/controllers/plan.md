# Plan

This section contains operations related to the configuration of future events.
This includes tasks, site accesses (and their connected device accesses), downtimes, personnel and organizations.

```python
plan_controller = client.plan
```

## Class Name

`PlanController`

## Methods

* [List Tasks](../../doc/controllers/plan.md#list-tasks)
* [Get Task](../../doc/controllers/plan.md#get-task)
* [List Task Categories](../../doc/controllers/plan.md#list-task-categories)
* [List Comments for Multiple Tasks](../../doc/controllers/plan.md#list-comments-for-multiple-tasks)
* [List Task Files](../../doc/controllers/plan.md#list-task-files)
* [Download Task File](../../doc/controllers/plan.md#download-task-file)
* [List Site Accesses](../../doc/controllers/plan.md#list-site-accesses)
* [Get Site Access](../../doc/controllers/plan.md#get-site-access)
* [List Device Accesses for Multiple Site Accesses](../../doc/controllers/plan.md#list-device-accesses-for-multiple-site-accesses)
* [Get Device Access](../../doc/controllers/plan.md#get-device-access)
* [List Downtime Events](../../doc/controllers/plan.md#list-downtime-events)
* [Get Downtime Event](../../doc/controllers/plan.md#get-downtime-event)
* [List Personnel](../../doc/controllers/plan.md#list-personnel)
* [Get Personnel](../../doc/controllers/plan.md#get-personnel)
* [List Organizations](../../doc/controllers/plan.md#list-organizations)
* [List Hse Incidents](../../doc/controllers/plan.md#list-hse-incidents)
* [Get Hse Incident](../../doc/controllers/plan.md#get-hse-incident)
* [List Worklog Items](../../doc/controllers/plan.md#list-worklog-items)
* [Get Worklog Item](../../doc/controllers/plan.md#get-worklog-item)


# List Tasks

Gets a list of tasks.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_tasks(self,
              timestamp_start,
              timestamp_end,
              device_ids=None,
              site_ids=None,
              category_ids=None,
              state=None,
              fields=None,
              page_size=50,
              page=1,
              use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `device_ids` | `List[int]` | Query, Optional | What devices to get tasks for.<br><br>**Constraints**: `>= 1` |
| `site_ids` | `List[int]` | Query, Optional | What sites to get tasks for.<br><br>**Constraints**: `>= 1` |
| `category_ids` | `List[int]` | Query, Optional | What task categories to include.<br><br>**Constraints**: `>= 1` |
| `state` | [`TaskStateEnum`](../../doc/models/task-state-enum.md) | Query, Optional | What state of tasks to get: resolved and unresolved. If not set, both resolved and unresolved tasks are included. |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `Task` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Task]`](../../doc/models/task.md).

## Example Usage

```python
timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

device_ids = [
    1,
    2,
    3
]

site_ids = [
    1,
    2,
    3
]

category_ids = [
    1,
    2,
    3
]

state = TaskStateEnum.UNRESOLVED

fields = [
    'taskId',
    'title'
]

page_size = 50

page = 1

use_utc = False

result = plan_controller.list_tasks(
    timestamp_start,
    timestamp_end,
    device_ids=device_ids,
    site_ids=site_ids,
    category_ids=category_ids,
    state=state,
    fields=fields,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "taskId": 10,
    "title": "Maintenance",
    "createdBy": {
      "firstName": "Greenbyte",
      "lastName": "Support"
    },
    "description": "maintenance on site",
    "category": {
      "categoryId": 5,
      "title": "Site visit without downtime"
    },
    "priority": "medium",
    "timestampStart": "2020-01-01T00:00:00",
    "timestampEnd": "2020-01-08T00:00:00",
    "state": "resolved",
    "resolved": true,
    "timestampResolved": "2020-01-08T00:00:00",
    "deviceIds": [
      21,
      22
    ],
    "siteIds": [],
    "siteAccessIds": [
      4177
    ],
    "downtimeEventIds": [],
    "statusIds": [],
    "numberOfComments": 3,
    "recurrence": null,
    "mainTaskId": null,
    "assignee": null,
    "metadata": [
      {
        "key": "Component",
        "value": "Yaw encoder"
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Task

Get a single task by ID.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def get_task(self,
            task_id,
            use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `int` | Template, Required | The id of the task to get.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Task`](../../doc/models/task.md).

## Example Usage

```python
task_id = 92

use_utc = False

result = plan_controller.get_task(
    task_id,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "taskId": 10,
  "title": "Maintenance",
  "createdBy": {
    "firstName": "Greenbyte",
    "lastName": "Support"
  },
  "description": "Notes go here",
  "category": {
    "categoryId": 32,
    "title": "Scheduled Maintenance"
  },
  "priority": "medium",
  "timestampStart": "2020-01-01T00:00:00.000Z",
  "timestampEnd": "2020-01-08T00:00:00.000Z",
  "state": "unresolved",
  "resolved": true,
  "timestampResolved": null,
  "deviceIds": [],
  "siteIds": [
    1
  ],
  "siteAccessIds": [],
  "downtimeEventIds": [],
  "statusIds": [],
  "numberOfComments": 3,
  "recurrence": {
    "duration": 1,
    "durationType": "year",
    "dateEnd": "2020-11-30"
  },
  "mainTaskId": 1544,
  "assignee": null,
  "metadata": []
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Task Categories

Gets a list of task categories.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_task_categories(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[TaskCategory]`](../../doc/models/task-category.md).

## Example Usage

```python
result = plan_controller.list_task_categories()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "categoryId": 10,
    "title": "Scheduled maintenance"
  },
  {
    "categoryId": 20,
    "title": "Unscheduled maintenance"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Comments for Multiple Tasks

Gets a list of comments belonging to one or more tasks with given taskIds.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_comments_for_multiple_tasks(self,
                                    task_ids,
                                    fields=None,
                                    page_size=50,
                                    page=1,
                                    use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_ids` | `List[int]` | Query, Required | An array of taskIds.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `TaskComment` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[TaskComment]`](../../doc/models/task-comment.md).

## Example Usage

```python
task_ids = [
    1,
    2,
    3
]

fields = [
    'commentId',
    'text'
]

page_size = 50

page = 1

use_utc = False

result = plan_controller.list_comments_for_multiple_tasks(
    task_ids,
    fields=fields,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "commentId": 10,
    "taskId": 1,
    "text": "Task started",
    "timestampCreated": "2020-01-01T00:00:00",
    "createdBy": {
      "firstName": "Greenbyte",
      "lastName": "Support"
    }
  },
  {
    "commentId": 11,
    "taskId": 2,
    "text": "Task finished",
    "timestampCreated": "2020-01-02T00:00:00",
    "createdBy": {
      "firstName": "Greenbyte",
      "lastName": "Support"
    }
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Task Files

Gets a list of files belonging to a task.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_task_files(self,
                   task_id,
                   fields=None,
                   page_size=50,
                   page=1,
                   use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `int` | Template, Required | The id of the task.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `TaskFile` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[TasksFilesResponse]`](../../doc/models/tasks-files-response.md).

## Example Usage

```python
task_id = 92

fields = [
    'fileName',
    'description'
]

page_size = 50

page = 1

use_utc = False

result = plan_controller.list_task_files(
    task_id,
    fields=fields,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "fileId": 501,
    "fileName": "Upgrade.docx",
    "timestampUploaded": "2020-05-29T16:12:34",
    "uploadedBy": {
      "firstName": "Greenbyte",
      "lastName": "Support"
    },
    "description": "Aerodynamic upgrade report",
    "category": "Reports"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Download Task File

Downloads a file belonging to a task.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def download_task_file(self,
                      task_id,
                      file_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `task_id` | `int` | Template, Required | The id of the task.<br><br>**Constraints**: `>= 1` |
| `file_id` | `int` | Template, Required | The id of the file.<br><br>**Constraints**: `>= 1` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
task_id = 92

file_id = 12

result = plan_controller.download_task_file(
    task_id,
    file_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Site Accesses

Gets a list of site accesses.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_site_accesses(self,
                      timestamp_start,
                      timestamp_end,
                      device_ids=None,
                      site_ids=None,
                      fields=None,
                      page_size=50,
                      page=1,
                      use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `device_ids` | `List[int]` | Query, Optional | What devices to get site accesses for.<br><br>**Constraints**: `>= 1` |
| `site_ids` | `List[int]` | Query, Optional | What sites to get site accesses for.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `SiteAccess` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[SiteAccess]`](../../doc/models/site-access.md).

## Example Usage

```python
timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

device_ids = [
    1,
    2,
    3
]

site_ids = [
    1,
    2,
    3
]

fields = [
    'siteAccessId',
    'timestampStart'
]

page_size = 50

page = 1

use_utc = False

result = plan_controller.list_site_accesses(
    timestamp_start,
    timestamp_end,
    device_ids=device_ids,
    site_ids=site_ids,
    fields=fields,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "siteAccessId": 10,
    "siteId": 18,
    "deviceIds": [
      11,
      12
    ],
    "taskIds": [
      66
    ],
    "siteAccessPersonnel": [
      {
        "personnelId": 1234,
        "firstName": "Andreas",
        "lastName": "Jonsson",
        "company": "Power Offtakers Inc.",
        "phoneNumber": "456-123",
        "vehicleRegistration": "ABC456",
        "comment": "Site access comment",
        "timestampStart": "2020-04-30T10:03:00",
        "timestampEnd": "2020-04-30T17:39:00"
      }
    ],
    "timestampStart": "2020-01-01T12:00:00",
    "timestampEndExpected": "2020-01-01T13:00:00",
    "timestampEnd": "2020-01-01T13:30:00",
    "logOnComment": "Investigating",
    "logOffComment": "All clear"
  },
  {
    "siteAccessId": 11,
    "siteId": 18,
    "deviceIds": [
      15
    ],
    "taskIds": [
      55,
      56
    ],
    "siteAccessPersonnel": [
      {
        "personnelId": 2345,
        "firstName": "Andrea",
        "lastName": "Larsson",
        "company": "Power Offtakers Inc.",
        "phoneNumber": "123-456",
        "vehicleRegistration": "ABC123",
        "comment": "Site access comment",
        "timestampStart": "2020-04-30T10:04:00",
        "timestampEnd": "2020-04-30T17:39:00"
      }
    ],
    "timestampStart": "2020-01-02T12:00:00",
    "timestampEndExpected": "2020-01-02T13:00:00",
    "timestampEnd": "2020-01-02T13:30:00",
    "logOnComment": "Investigating",
    "logOffComment": "All clear"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Site Access

Gets a specific site access.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def get_site_access(self,
                   site_access_id,
                   use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_access_id` | `int` | Template, Required | The id of the site access.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SiteAccess`](../../doc/models/site-access.md).

## Example Usage

```python
site_access_id = 10

use_utc = False

result = plan_controller.get_site_access(
    site_access_id,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "siteAccessId": 10,
  "siteId": 18,
  "deviceIds": [
    11,
    12
  ],
  "taskIds": [
    66
  ],
  "siteAccessPersonnel": [
    {
      "personnelId": 1234,
      "firstName": "Andreas",
      "lastName": "Jonsson",
      "company": "Power Offtakers Inc.",
      "phoneNumber": "456-123",
      "vehicleRegistration": "ABC456",
      "comment": "Site access comment",
      "timestampStart": "2020-04-30T10:03:00",
      "timestampEnd": "2020-04-30T17:39:00"
    }
  ],
  "timestampStart": "2020-01-01T12:00:00",
  "timestampEndExpected": "2020-01-01T13:00:00",
  "timestampEnd": "2020-01-01T13:30:00",
  "logOnComment": "Investigating",
  "logOffComment": "All clear"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Device Accesses for Multiple Site Accesses

Gets a list of device accesses belonging to site accesses with specified SiteAccessIds.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_device_accesses_for_multiple_site_accesses(self,
                                                   site_access_ids,
                                                   fields=None,
                                                   page_size=50,
                                                   page=1,
                                                   use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `site_access_ids` | `List[int]` | Query, Required | An array of siteAccessIds.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `DeviceAccess` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DeviceAccess]`](../../doc/models/device-access.md).

## Example Usage

```python
site_access_ids = [
    1,
    2
]

fields = [
    'deviceAccessId',
    'siteId'
]

page_size = 50

page = 1

use_utc = False

result = plan_controller.list_device_accesses_for_multiple_site_accesses(
    site_access_ids,
    fields=fields,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceAccessId": 1504,
    "siteId": 50,
    "siteAccessId": 1,
    "deviceIds": [
      15
    ],
    "personnelIds": [
      11,
      12
    ],
    "taskIds": [
      55
    ],
    "timestampStart": "2020-01-02T12:00:00",
    "timestampEnd": "2020-01-02T12:55:00",
    "timestampEndExpected": "2020-01-02T13:00:00",
    "logOnComment": "TOC at 12:01",
    "logOffComment": "Access completed"
  },
  {
    "deviceAccessId": 1560,
    "siteId": 50,
    "siteAccessId": 2,
    "deviceIds": [
      15
    ],
    "personnelIds": [
      11,
      12
    ],
    "taskIds": [
      55
    ],
    "timestampStart": "2020-01-02T13:00:00",
    "timestampEnd": "2020-01-02T13:55:00",
    "timestampEndExpected": "2020-01-02T14:00:00",
    "logOnComment": "TOC at 13:01",
    "logOffComment": "Access completed"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Device Access

Get a single device access by ID.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def get_device_access(self,
                     device_access_id,
                     use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_access_id` | `int` | Template, Required | The id of the device access to get.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeviceAccess`](../../doc/models/device-access.md).

## Example Usage

```python
device_access_id = 38

use_utc = False

result = plan_controller.get_device_access(
    device_access_id,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "deviceAccessId": 1542,
  "siteId": 50,
  "deviceIds": [
    15
  ],
  "personnelIds": [
    11,
    12
  ],
  "taskIds": [
    55
  ],
  "timestampStart": "2020-01-02T12:00:00",
  "timestampEnd": "2020-01-02T12:55:00",
  "timestampEndExpected": "2020-01-02T13:00:00",
  "logOnComment": "TOC at 12:01",
  "logOffComment": "Access completed"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Downtime Events

Gets a list of downtime events.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_downtime_events(self,
                        timestamp_start,
                        timestamp_end,
                        device_ids=None,
                        site_ids=None,
                        fields=None,
                        page_size=50,
                        page=1,
                        use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `device_ids` | `List[int]` | Query, Optional | What devices to get downtime events for.<br><br>**Constraints**: `>= 1` |
| `site_ids` | `List[int]` | Query, Optional | What sites to get downtime events for.<br><br>**Constraints**: `>= 1` |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `DowntimeEvent` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DowntimeEvent]`](../../doc/models/downtime-event.md).

## Example Usage

```python
timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

device_ids = [
    1,
    2,
    3
]

site_ids = [
    1,
    2,
    3
]

fields = [
    'deviceIds',
    'timestampStart'
]

page_size = 50

page = 1

use_utc = False

result = plan_controller.list_downtime_events(
    timestamp_start,
    timestamp_end,
    device_ids=device_ids,
    site_ids=site_ids,
    fields=fields,
    page_size=page_size,
    page=page,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "downtimeEventId": 1,
    "deviceIds": [
      1,
      2,
      3
    ],
    "timestampStart": "2020-01-01T00:00:00",
    "timestampEnd": "2020-01-02T00:00:00",
    "comment": "Planned downtime",
    "siteIds": [],
    "taskIds": [
      1358
    ],
    "remainingCapacityPercentage": 10
  },
  {
    "downtimeEventId": 2,
    "deviceIds": [
      1,
      2,
      3
    ],
    "timestampStart": "2020-01-10T00:00:00",
    "timestampEnd": "2020-01-12T00:00:00",
    "comment": "Unplanned downtime",
    "siteIds": [
      1
    ],
    "taskIds": [
      1359
    ],
    "remainingCapacityPercentage": 0
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Downtime Event

Gets a single downtime event by ID.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def get_downtime_event(self,
                      downtime_event_id,
                      use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `downtime_event_id` | `int` | Template, Required | The id of the downtime event to get.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DowntimeEvent`](../../doc/models/downtime-event.md).

## Example Usage

```python
downtime_event_id = 168

use_utc = False

result = plan_controller.get_downtime_event(
    downtime_event_id,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "downtimeEventId": 2,
  "deviceIds": [
    1,
    2,
    3
  ],
  "timestampStart": "2020-01-10T00:00:00",
  "timestampEnd": "2020-01-12T00:00:00",
  "comment": "Unplanned downtime",
  "siteIds": [
    1
  ],
  "taskIds": [
    1359
  ],
  "remainingCapacityPercentage": 5.5
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Personnel

Gets a list of personnel.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_personnel(self,
                  fields=None,
                  page_size=50,
                  page=1)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fields` | `List[str]` | Query, Optional | Which fields to include in the response. Valid fields are those defined in the `Personnel` schema (See Response Type). By default all fields are included. |
| `page_size` | `int` | Query, Optional | The number of items to return per page.<br><br>**Default**: `50` |
| `page` | `int` | Query, Optional | Which page to return when the number of items exceed the page size.<br><br>**Default**: `1` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Personnel]`](../../doc/models/personnel.md).

## Example Usage

```python
fields = [
    'lastName',
    'phone'
]

page_size = 50

page = 1

result = plan_controller.list_personnel(
    fields=fields,
    page_size=page_size,
    page=page
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "personnelId": 5,
    "firstName": "Greenbyte",
    "lastName": "Support",
    "email": "support@greenbyte.com",
    "phone": "123-456",
    "mobile": "654-321",
    "organization": {
      "organizationId": 10,
      "name": "Power Offtakers Inc.",
      "email": "support@power-offtakers.example.com",
      "phone": "456-789"
    },
    "qualifications": [
      {
        "qualificationId": 85,
        "manufacturer": "GE",
        "qualificationType": "AP",
        "qualificationDescription": "Authorized Person"
      }
    ],
    "siteInductions": [
      {
        "siteInductionId": 43,
        "siteId": 1,
        "dateExpires": "2020-12-01"
      }
    ]
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Personnel

Gets a single personnel by ID.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def get_personnel(self,
                 personnel_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `personnel_id` | `int` | Template, Required | The id of the personnel to get.<br><br>**Constraints**: `>= 1` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Personnel`](../../doc/models/personnel.md).

## Example Usage

```python
personnel_id = 128

result = plan_controller.get_personnel(personnel_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "personnelId": 5,
  "firstName": "Greenbyte",
  "lastName": "Support",
  "email": "support@greenbyte.com",
  "phone": "123-456",
  "mobile": "654-321",
  "organization": {
    "organizationId": 10,
    "name": "Power Offtakers Inc.",
    "email": "support@power-offtakers.example.com",
    "phone": "456-789"
  },
  "qualifications": [
    {
      "qualificationId": 85,
      "manufacturer": "GE",
      "qualificationType": "AP",
      "qualificationDescription": "Authorized Person"
    }
  ],
  "siteInductions": [
    {
      "siteInductionId": 43,
      "siteId": 1,
      "dateExpires": "2020-12-01"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Organizations

Gets a list of organizations.

_🔐 This endpoint requires the **Plan** endpoint permission._

```python
def list_organizations(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[Organization]`](../../doc/models/organization.md).

## Example Usage

```python
result = plan_controller.list_organizations()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "organizationId": 10,
    "name": "Power Offtakers Inc.",
    "email": "support@power-offtakers.example.com",
    "phone": "456-789"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Hse Incidents

Gets a list of HSE incidents.

_🔐 This endpoint requires the **Plan** endpoint permission._

_This is a beta feature. Some details might change before it is released as a stable version._

```python
def list_hse_incidents(self,
                      timestamp_start,
                      timestamp_end,
                      site_ids=None,
                      state=None,
                      category=None,
                      use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `site_ids` | `List[int]` | Query, Optional | Which sites to get HSE incidents for.<br><br>**Constraints**: `>= 1` |
| `state` | [`StateEnum`](../../doc/models/state-enum.md) | Query, Optional | Retrieve HSE incidents with state: resolved or unresolved.<br>If not set, both resolved and unresolved HSE incidents are included. |
| `category` | [`HSECategoryEnum`](../../doc/models/hse-category-enum.md) | Query, Optional | Retrieve HSE incidents with a specific category.<br>If not set, HSE incidents of all categories are included. |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[HseIncidentsResponse]`](../../doc/models/hse-incidents-response.md).

## Example Usage

```python
timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

site_ids = [
    1,
    2,
    3
]

state = StateEnum.UNRESOLVED

category = HSECategoryEnum.ACCIDENT

use_utc = False

result = plan_controller.list_hse_incidents(
    timestamp_start,
    timestamp_end,
    site_ids=site_ids,
    state=state,
    category=category,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "hseIncidentId": 10,
    "siteId": 5,
    "deviceId": 1,
    "timestamp": "2022-12-18T09:45:00",
    "hseCategory": "HazardObservation",
    "lostTimeInjury": false,
    "incidentDescription": "Broken ladder",
    "resolved": false,
    "resolvedTimestamp": null
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Hse Incident

Get a single HSE incident by ID.

_🔐 This endpoint requires the **Plan** endpoint permission._

_This is a beta feature. Some details might change before it is released as a stable version._

```python
def get_hse_incident(self,
                    hse_incident_id,
                    use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `hse_incident_id` | `int` | Template, Required | The id of the HSE incident to get.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`HseIncidentsResponse`](../../doc/models/hse-incidents-response.md).

## Example Usage

```python
hse_incident_id = 1

use_utc = False

result = plan_controller.get_hse_incident(
    hse_incident_id,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "hseIncidentId": 10,
  "siteId": 5,
  "deviceId": 1,
  "timestamp": "2022-12-18T09:45:00",
  "hseCategory": "HazardObservation",
  "lostTimeInjury": false,
  "incidentDescription": "Broken ladder",
  "resolved": false,
  "resolvedTimestamp": null
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# List Worklog Items

Gets a list of worklog items.

_🔐 This endpoint requires the **Plan** endpoint permission._

_This is a beta feature. Some details might change before it is released as a stable version._

```python
def list_worklog_items(self,
                      timestamp_start,
                      timestamp_end,
                      site_ids=None,
                      use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp_start` | `datetime` | Query, Required | The beginning of the time interval to get data for (inclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The start timestamp **is** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `timestamp_end` | `datetime` | Query, Required | The end of the time interval to get data for (exclusive),<br>in [RFC 3339, section 5.6](https://tools.ietf.org/html/rfc3339#section-5.6)<br>**date-time** format:<br><br>* Timestamps ending with 'Z' are treated as UTC. Example: "2020-01-01T00:00:00Z"<br>* Time zone (UTC) offset timestamps ending with '+HH:mm'/"-HH:mm" are also supported. Example: "2020-01-01T02:00:00-02:00"<br>* Other timestamps are treated as being in the time zone configured in the Greenbyte Platform. Example: "2020-01-01T00:00:00"<br><br>The end timestamp is **not** included in the time interval: for<br>example, to select the full month of March 2020, set<br>`timestampStart` to "2020-03-01T00:00:00" and `timestampEnd` to<br>"2020-04-01T00:00:00".<br><br>Timestamps selected in the portal will by default be in UTC. |
| `site_ids` | `List[int]` | Query, Optional | What sites to get worklog items for.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[WorklogResponse]`](../../doc/models/worklog-response.md).

## Example Usage

```python
timestamp_start = dateutil.parser.parse('01/01/2024 00:00:00')

timestamp_end = dateutil.parser.parse('01/08/2024 00:00:00')

site_ids = [
    1,
    2,
    3
]

use_utc = False

result = plan_controller.list_worklog_items(
    timestamp_start,
    timestamp_end,
    site_ids=site_ids,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "worklogItemId": 10,
    "timestamp": "2023-01-08T00:00:00",
    "siteId": 5,
    "hoursWorked": 2.5,
    "comment": "Inverter B Offline With Repeated Fault\n- Work Performed: INV B was cleaned\n"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |


# Get Worklog Item

Get a single worklog item by ID.

_🔐 This endpoint requires the **Plan** endpoint permission._

_This is a beta feature. Some details might change before it is released as a stable version._

```python
def get_worklog_item(self,
                    worklog_item_id,
                    use_utc=False)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `worklog_item_id` | `int` | Template, Required | The id of the worklog item to get.<br><br>**Constraints**: `>= 1` |
| `use_utc` | `bool` | Query, Optional | Set to true to get timestamps in UTC.<br><br>**Default**: `False` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WorklogResponse`](../../doc/models/worklog-response.md).

## Example Usage

```python
worklog_item_id = 218

use_utc = False

result = plan_controller.get_worklog_item(
    worklog_item_id,
    use_utc=use_utc
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "worklogItemId": 10,
  "timestamp": "2023-01-08T00:00:00",
  "siteId": 5,
  "hoursWorked": 2.5,
  "comment": "Inverter B Offline With Repeated Fault.\nWork Performed - INV B was cleaned\n"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | The request cannot be fulfilled due to bad syntax. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |
| 401 | The request is missing a valid API key. | `APIException` |
| 403 | One of the following:<br><br>* The API key does not authorize access to the requested endpoint because of a missing endpoint permission.<br>* The API key does not authorize access to the requested data. Devices, sites or data signals can be limited. | `APIException` |
| 404 | The requested resource could not be found. | `APIException` |
| 405 | The HTTP method is not allowed for the endpoint. | `APIException` |
| 429 | The API key has been used in too many requests in a given amount<br>of time. The following headers will be set in the response:<br><br>* `X-Rate-Limit-Limit` – The rate limit period (for example<br>  "1m", "12h", or "1d").<br>* `X-Rate-Limit-Remaining` – The remaining number of requests<br>  for this period.<br>* `X-Rate-Limit-Reset` – The UTC timestamp string (in ISO 8601<br>  format) when the remaining number of requests resets.<br><br>The limit is currently 1,000 requests/minute per API key and IP<br>address. | [`ProblemDetailsException`](../../doc/models/problem-details-exception.md) |

