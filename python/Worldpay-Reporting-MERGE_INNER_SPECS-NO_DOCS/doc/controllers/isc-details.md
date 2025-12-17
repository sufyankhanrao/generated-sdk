# ISC Details

```python
isc_details_controller = client.isc_details
```

## Class Name

`ISCDetailsController`


# Get List of Independent Sales Channel

Retrieves list of independent sales channel based on the license in use.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_list_of_independent_sales_channel(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[ISCDetails]`](../../doc/models/isc-details.md).

## Example Usage

```python
result = isc_details_controller.get_list_of_independent_sales_channel()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError3Exception`](../../doc/models/error-response-error-3-exception.md) |

