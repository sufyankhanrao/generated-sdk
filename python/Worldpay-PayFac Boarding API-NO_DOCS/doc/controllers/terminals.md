# Terminals

Resources to create and maintain Terminal Settings for a PayFac SubMerchant

```python
terminals_controller = client.terminals
```

## Class Name

`TerminalsController`

## Methods

* [Get Supported Terminals](../../doc/controllers/terminals.md#get-supported-terminals)
* [Get Terminals](../../doc/controllers/terminals.md#get-terminals)
* [Update Terminals](../../doc/controllers/terminals.md#update-terminals)
* [Create Terminals](../../doc/controllers/terminals.md#create-terminals)
* [Get Terminalsbatchclosetime](../../doc/controllers/terminals.md#get-terminalsbatchclosetime)
* [Get One Terminal](../../doc/controllers/terminals.md#get-one-terminal)
* [Update Terminal](../../doc/controllers/terminals.md#update-terminal)
* [Delete Terminal](../../doc/controllers/terminals.md#delete-terminal)
* [Get Var Sheets](../../doc/controllers/terminals.md#get-var-sheets)


# Get Supported Terminals

URI to obtain a list of all supported terminals and their related information for a submerchant

```python
def get_supported_terminals(self,
                           v_correlation_id,
                           id,
                           content_type="application/json",
                           template_mid=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |
| `template_mid` | `str` | Query, Optional | Template Mid associated with the chain code - used for building terminals |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SupportedTerminalsGetResponse`](../../doc/models/supported-terminals-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

template_mid = '4445000000001'

result = terminals_controller.get_supported_terminals(
    v_correlation_id,
    id,
    content_type=content_type,
    template_mid=template_mid
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


# Get Terminals

URI to obtain a list of all terminals and their related information for a submerchant

```python
def get_terminals(self,
                 v_correlation_id,
                 id,
                 content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsSuccessResponse`](../../doc/models/terminals-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

result = terminals_controller.get_terminals(
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
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Update Terminals

URI to update information for all the terminals for a submerchant

```python
def update_terminals(self,
                    v_correlation_id,
                    id,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`TerminalsForUpdate`](../../doc/models/terminals-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsUpdateResponse`](../../doc/models/terminals-update-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = TerminalsForUpdate(
    batch_close_time='0430',
    batch_close_type='H',
    batch_turn_off='No'
)

result = terminals_controller.update_terminals(
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
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Create Terminals

URI to add a terminal from the Template MID to a Sub-Merchant. Be careful to pass the tid and not the terminal id. The tid will be a 1 to 3 digit number and is labeled “tid” in the Supported Terminals response.)

```python
def create_terminals(self,
                    v_correlation_id,
                    id,
                    body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `body` | [`TerminalToCreate`](../../doc/models/terminal-to-create.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsSuccessResponse`](../../doc/models/terminals-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

body = TerminalToCreate(
    template_mid='400000000002',
    tid='1',
    quantity='2'
)

result = terminals_controller.create_terminals(
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
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Get Terminalsbatchclosetime

URI to obtain batch close time for all the terminals.

```python
def get_terminalsbatchclosetime(self,
                               v_correlation_id,
                               id,
                               content_type="application/json",
                               page_number=None,
                               page_size=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |
| `page_number` | `int` | Query, Optional | This is the page number that needs to be retrieved <br> Default is page number 1 |
| `page_size` | `int` | Query, Optional | Number of records that needs to be retrieved per page <br> Default is 25 records per page and the max limit is 2000. |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalsBatchCloseResponse`](../../doc/models/terminals-batch-close-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

content_type = 'application/json'

page_number = 2

page_size = 10

result = terminals_controller.get_terminalsbatchclosetime(
    v_correlation_id,
    id,
    content_type=content_type,
    page_number=page_number,
    page_size=page_size
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


# Get One Terminal

URI to obtain information for one terminal for a submerchant

```python
def get_one_terminal(self,
                    v_correlation_id,
                    id,
                    tid,
                    content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `tid` | `str` | Template, Required | The terminal number (1-3 digits) |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalByTIDGetResponse`](../../doc/models/terminal-by-tid-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

tid = 'tid0'

content_type = 'application/json'

result = terminals_controller.get_one_terminal(
    v_correlation_id,
    id,
    tid,
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


# Update Terminal

URI to update information for a terminal for a submerchant

```python
def update_terminal(self,
                   v_correlation_id,
                   id,
                   tid,
                   body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `tid` | `str` | Template, Required | The terminal number (1-3 digits) |
| `body` | [`TerminalForUpdate`](../../doc/models/terminal-for-update.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalByTIDGetResponse`](../../doc/models/terminal-by-tid-get-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

tid = 'tid0'

body = TerminalForUpdate()

result = terminals_controller.update_terminal(
    v_correlation_id,
    id,
    tid,
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
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |


# Delete Terminal

URI to disable a terminal for a submerchant

```python
def delete_terminal(self,
                   v_correlation_id,
                   id,
                   tid,
                   content_type="application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `str` | Template, Required | The resource ID of the submerchant |
| `tid` | `str` | Template, Required | The terminal number (1-3 digits) |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DefaultSuccessResponse`](../../doc/models/default-success-response.md).

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = 'id0'

tid = 'tid0'

content_type = 'application/json'

result = terminals_controller.delete_terminal(
    v_correlation_id,
    id,
    tid,
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
| 403 | Forbidden | [`M403ErrorResponseException`](../../doc/models/m403-error-response-exception.md) |
| 404 | Not Found | [`M404ErrorResponseException`](../../doc/models/m404-error-response-exception.md) |
| 500 | Server Error | [`M500ErrorResponseException`](../../doc/models/m500-error-response-exception.md) |


# Get Var Sheets

URI to obtain all the var sheets for a submerchant

```python
def get_var_sheets(self,
                  v_correlation_id,
                  id,
                  tid,
                  content_type="application/pdf or application/json")
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `v_correlation_id` | `uuid\|str` | Header, Required | The unique UUID that is sent in each request |
| `id` | `uuid\|str` | Template, Required | The resource ID of the submerchant |
| `tid` | `str` | Template, Required | The terminal number (1-3 digits) |
| `content_type` | `str` | Header, Optional | The original media type of the resource<br><br>**Default**: `"application/pdf or application/json"` |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
v_correlation_id = '0000139e-0000-0000-0000-000000000000'

id = '00001770-0000-0000-0000-000000000000'

tid = 'tid0'

content_type = 'application/pdf or application/json'

result = terminals_controller.get_var_sheets(
    v_correlation_id,
    id,
    tid,
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
| 400 | Bad Request | `APIException` |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
| 404 | Not Found | `APIException` |
| 500 | Server Error | `APIException` |

