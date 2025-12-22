# API

```python
client_controller = client.client
```

## Class Name

`APIController`

## Methods

* [Get Non Scalar Content](../../doc/controllers/api.md#get-non-scalar-content)
* [Get Scalar String Content](../../doc/controllers/api.md#get-scalar-string-content)
* [Get Scalar Non Null String](../../doc/controllers/api.md#get-scalar-non-null-string)
* [Get Scalar Number Content](../../doc/controllers/api.md#get-scalar-number-content)


# Get Non Scalar Content

```python
def get_non_scalar_content(self,
                          test_case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test_case` | [`SelectorEnum`](../../doc/models/selector-enum.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResponsesNonScalarContentResponse`](../../doc/models/responses-non-scalar-content-response.md).

## Example Usage

```python
result = client_controller.get_non_scalar_content()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Scalar String Content

```python
def get_scalar_string_content(self,
                             test_case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test_case` | [`SelectorEnum`](../../doc/models/selector-enum.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = client_controller.get_scalar_string_content()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Scalar Non Null String

```python
def get_scalar_non_null_string(self,
                              test_case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test_case` | [`SelectorEnum`](../../doc/models/selector-enum.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = client_controller.get_scalar_non_null_string()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Scalar Number Content

```python
def get_scalar_number_content(self,
                             test_case=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `test_case` | [`SelectorEnum`](../../doc/models/selector-enum.md) | Query, Optional | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `int`.

## Example Usage

```python
result = client_controller.get_scalar_number_content()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

