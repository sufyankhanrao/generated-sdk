# Reports API

```python
reports_api_controller = client.reports_api
```

## Class Name

`ReportsAPIController`


# Download Report

To create a new user via API, please make a call to /users/create with the following parameters.

```python
def download_report(self,
                   accept,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accept` | `str` | Header, Required | - |
| `body` | [`Report`](../../doc/models/report.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
accept = 'application/vnd.ms-excel'

body = Report(
    status=EnvelopeStatusEnum.EXECUTED,
    creation_date_from='2022-01-01',
    creation_date_to='2022-04-01',
    include_fields='false'
)

result = reports_api_controller.download_report(
    accept,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

