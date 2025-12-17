# API

```python
client_controller = client.client
```

## Class Name

`APIController`

## Methods

* [Try Api Call](../../doc/controllers/api.md#try-api-call)
* [Try Post Api Call](../../doc/controllers/api.md#try-post-api-call)
* [Retry Post Api Call](../../doc/controllers/api.md#retry-post-api-call)
* [Retry Api Call](../../doc/controllers/api.md#retry-api-call)
* [Dont Retry Api Call](../../doc/controllers/api.md#dont-retry-api-call)
* [Retry Send File](../../doc/controllers/api.md#retry-send-file)


# Try Api Call

```python
def try_api_call(self,
                case,
                max_retries=None,
                timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `case` | `str` | Template, Required | Try api call for this case |
| `max_retries` | `int` | Header, Optional | Maximum number of allowed retries |
| `timeout` | `int` | Header, Optional | Timeout for all requests in seconds |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
case = 'case0'

result = client_controller.try_api_call(case)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Try Post Api Call

```python
def try_post_api_call(self,
                     max_retries=None,
                     timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_retries` | `int` | Header, Optional | Maximum number of allowed retries |
| `timeout` | `int` | Header, Optional | Timeout for all requests in seconds |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
result = client_controller.try_post_api_call()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retry Post Api Call

```python
def retry_post_api_call(self,
                       max_retries=None,
                       timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_retries` | `int` | Header, Optional | Maximum number of allowed retries |
| `timeout` | `int` | Header, Optional | Timeout for all requests in seconds |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
result = client_controller.retry_post_api_call()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retry Api Call

```python
def retry_api_call(self,
                  max_retries=None,
                  retry_after=None,
                  timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_retries` | `int` | Header, Optional | Maximum number of allowed retries |
| `retry_after` | `int` | Header, Optional | Retry after in seconds |
| `timeout` | `int` | Header, Optional | Timeout for all requests in seconds |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
result = client_controller.retry_api_call()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Dont Retry Api Call

```python
def dont_retry_api_call(self,
                       max_retries=None,
                       timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `max_retries` | `int` | Header, Optional | Maximum number of allowed retries |
| `timeout` | `int` | Header, Optional | Timeout for all requests in seconds |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
result = client_controller.dont_retry_api_call()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Retry Send File

```python
def retry_send_file(self,
                   file,
                   max_retries=None,
                   retry_after=None,
                   timeout=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file` | `typing.BinaryIO` | Body, Required | - |
| `max_retries` | `int` | Header, Optional | Maximum number of allowed retries |
| `retry_after` | `int` | Header, Optional | Retry after in seconds |
| `timeout` | `int` | Header, Optional | Timeout for all requests in seconds |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
file = FileWrapper(Path('dummy_file').open('rb'), 'optional-content-type')

result = client_controller.retry_send_file(file)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

