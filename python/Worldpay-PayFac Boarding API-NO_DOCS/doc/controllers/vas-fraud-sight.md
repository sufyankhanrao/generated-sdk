# VAS-Fraud Sight

```python
vas_fraud_sight_controller = client.vas_fraud_sight
```

## Class Name

`VASFraudSightController`

## Methods

* [Get Fraud Sight Supported Rules](../../doc/controllers/vas-fraud-sight.md#get-fraud-sight-supported-rules)
* [Get Fraud Sight Rules for Group](../../doc/controllers/vas-fraud-sight.md#get-fraud-sight-rules-for-group)
* [Get Fraud Sight Rule Groups](../../doc/controllers/vas-fraud-sight.md#get-fraud-sight-rule-groups)
* [Update Fraud Sight](../../doc/controllers/vas-fraud-sight.md#update-fraud-sight)
* [Enable Fraud Sight](../../doc/controllers/vas-fraud-sight.md#enable-fraud-sight)
* [Delete Fraud Sight](../../doc/controllers/vas-fraud-sight.md#delete-fraud-sight)


# Get Fraud Sight Supported Rules

URI to get the supported fraudsight rule groups for a submerchant.

```python
def get_fraud_sight_supported_rules(self,
                                   v_correlation_id,
                                   id,
                                   content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FraudSightGroupResponse`](../../doc/models/fraud-sight-group-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = vas_fraud_sight_controller.get_fraud_sight_supported_rules(
    v_correlation_id,
    id,
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Get Fraud Sight Rules for Group

URI to get the detailed rules for a fraudsight rule group.

```python
def get_fraud_sight_rules_for_group(self,
                                   v_correlation_id,
                                   id,
                                   groupname,
                                   content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `groupname` | `str` | Template, Required | The rule group resource id |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FraudSightResponse`](../../doc/models/fraud-sight-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

groupname = 'groupname6'

content_type = 'application/json'

result = vas_fraud_sight_controller.get_fraud_sight_rules_for_group(
    v_correlation_id,
    id,
    groupname,
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Get Fraud Sight Rule Groups

URI to get the current rule groups for a submerchant.

```python
def get_fraud_sight_rule_groups(self,
                               v_correlation_id,
                               id,
                               content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FraudSightGroupResponse`](../../doc/models/fraud-sight-group-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = vas_fraud_sight_controller.get_fraud_sight_rule_groups(
    v_correlation_id,
    id,
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Update Fraud Sight

URI to update rules for FraudSight for a submerchant

```python
def update_fraud_sight(self,
                      v_correlation_id,
                      id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`RuleGroup`](../../doc/models/rule-group.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FraudSightGroupResponse`](../../doc/models/fraud-sight-group-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = RuleGroup(
    group_name='ECNP',
    description='Pre Network - Decision CNP and Non EMV CP'
)

result = vas_fraud_sight_controller.update_fraud_sight(
    v_correlation_id,
    id,
    body
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Enable Fraud Sight

URI to enable FraudSight rules for a submerchant.

```python
def enable_fraud_sight(self,
                      v_correlation_id,
                      id,
                      body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`RuleGroup`](../../doc/models/rule-group.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`FraudSightGroupResponse`](../../doc/models/fraud-sight-group-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = RuleGroup(
    group_name='ECNP',
    description='Pre Network - Decision CNP and Non EMV CP'
)

result = vas_fraud_sight_controller.enable_fraud_sight(
    v_correlation_id,
    id,
    body
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
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Delete Fraud Sight

URI to disable fraudsight for a Submerchant.

```python
def delete_fraud_sight(self,
                      v_correlation_id,
                      id,
                      content_type='application/json')
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `'application/json'` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = vas_fraud_sight_controller.delete_fraud_sight(
    v_correlation_id,
    id,
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
| 401 | Unauthorized | [`M401ErrorResponseException`](../../doc/models/m401-error-response-exception.md) |
| 403 | Forbidden | [`M403ErrorResponseFormatException`](../../doc/models/m403-error-response-format-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |

