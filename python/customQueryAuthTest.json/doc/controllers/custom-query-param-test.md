# Custom Query Param Test

```python
custom_query_param_test_controller = client.custom_query_param_test
```

## Class Name

`CustomQueryParamTestController`

## Methods

* [Get Custom Query Parameter Testing](../../doc/controllers/custom-query-param-test.md#get-custom-query-parameter-testing)
* [Get Custom Query Param Skipped Authentication](../../doc/controllers/custom-query-param-test.md#get-custom-query-param-skipped-authentication)


# Get Custom Query Parameter Testing

```python
def get_custom_query_parameter_testing(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = custom_query_param_test_controller.get_custom_query_parameter_testing()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Custom Query Param Skipped Authentication

:information_source: **Note** This endpoint does not require authentication.

```python
def get_custom_query_param_skipped_authentication(self)
```

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `str`.

## Example Usage

```python
result = custom_query_param_test_controller.get_custom_query_param_skipped_authentication()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

