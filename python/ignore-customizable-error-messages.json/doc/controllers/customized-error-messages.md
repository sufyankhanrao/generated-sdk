# Customized Error Messages

Contains all endpoints to test the customized error messages behavior.

```python
customized_error_messages_controller = client.customized_error_messages
```

## Class Name

`CustomizedErrorMessagesController`

## Methods

* [Endpoint Level Error Template Message](../../doc/controllers/customized-error-messages.md#endpoint-level-error-template-message)
* [Override Global Level Error Messages](../../doc/controllers/customized-error-messages.md#override-global-level-error-messages)


# Endpoint Level Error Template Message

This endpoint contains cases for customized error templates at endpoint level.

```python
def endpoint_level_error_template_message(self)
```

## Response Type

`Any`

## Example Usage

```python
result = customized_error_messages_controller.endpoint_level_error_template_message()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Local error message for 401 | [`ErrorModel3Exception`](../../doc/models/error-model-3-exception.md) |
| 402 | Local error message for 402 | [`ErrorModel2Exception`](../../doc/models/error-model-2-exception.md) |
| 500 | Local error message for 500 | `APIException` |
| Default | Local error message for default case. | [`ErrorModel1Exception`](../../doc/models/error-model-1-exception.md) |


# Override Global Level Error Messages

This endpoint overrides the cases for customized errors configured at global level.

```python
def override_global_level_error_messages(self)
```

## Response Type

`Any`

## Example Usage

```python
result = customized_error_messages_controller.override_global_level_error_messages()
print(result)
```

