# Resource ID

```python
resource_id_controller = client.resource_id
```

## Class Name

`ResourceIDController`


# Get Submerchant Resourse Id by Mid

URI to get the identifier for a PayFac submerchant resource <br/> <br/> For an existing Sub-Merchant, if you want to get the resource ID that is used in all the resources, then this resource can be used with the Sub-Merchant Merchant Identifier mid. In the case of a retrieval request, the system does not require an accompanying Request body.

```python
def get_submerchant_resourse_id_by_mid(self,
                                      v_correlation_id,
                                      mid,
                                      content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `mid` | `str` | Template, Required | The merchant identifier of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResourceIdGetResponse`](../../doc/models/resource-id-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

mid = 'mid0'

content_type = 'application/json'

result = resource_id_controller.get_submerchant_resourse_id_by_mid(
    v_correlation_id,
    mid,
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

