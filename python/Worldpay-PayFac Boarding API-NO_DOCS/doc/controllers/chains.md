# Chains

resource to obtain information about the chain codes of a PayFac

```python
chains_controller = client.chains
```

## Class Name

`ChainsController`

## Methods

* [Get Chains](../../doc/controllers/chains.md#get-chains)
* [Get Chain Config](../../doc/controllers/chains.md#get-chain-config)


# Get Chains

URI to get the all the chain codes for a PayFac.

```python
def get_chains(self,
              v_correlation_id,
              content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChainsGetResponse`](../../doc/models/chains-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

content_type = 'application/json'

result = chains_controller.get_chains(
    v_correlation_id,
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
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Get Chain Config

URI to get the configuration for a specific chain code

```python
def get_chain_config(self,
                    v_correlation_id,
                    chain_code,
                    content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `chain_code` | `str` | Template, Required | The chain code |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChainConfig`](../../doc/models/chain-config.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

chain_code = 'chainCode4'

content_type = 'application/json'

result = chains_controller.get_chain_config(
    v_correlation_id,
    chain_code,
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
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |

