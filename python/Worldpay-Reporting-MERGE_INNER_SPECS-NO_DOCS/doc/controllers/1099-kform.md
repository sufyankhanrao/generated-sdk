# 1099 Kform

```python
m_1099_kform_controller = client.m1099_kform
```

## Class Name

`M1099kformController`


# Get Form

Resource to download 1099k form for a specific merchant id.

```python
def get_form(self,
            merchant_id,
            v_correlation_id=None,
            taxyear=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Header, Required | Unique identifier of the merchant (card acceptor).<br><br>**Constraints**: *Maximum Length*: `16` |
| `v_correlation_id` | `uuid\|str` | Header, Optional | Correlation Id |
| `taxyear` | `int` | Query, Optional | Tax year for which 1099k to be generated.<br><br>**Constraints**: `>= 4`, `<= 4` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `binary`.

## Example Usage

```python
merchant_id = '9945091191791'

v_correlation_id = 'a0efdf0f-eb0b-4353-80bb-ec520e02885e'

result = m_1099_k_form_controller.get_form(
    merchant_id,
    v_correlation_id=v_correlation_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Default errors | [`ErrorResponseError4Exception`](../../doc/models/error-response-error-4-exception.md) |

