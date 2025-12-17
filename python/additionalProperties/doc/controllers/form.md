# Form

```python
form_controller = client.form
```

## Class Name

`FormController`


# Upload Form Enabled Any

```python
def upload_form_enabled_any(self,
                           non_inherit_enabled_any,
                           any_of_additional_properties)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `non_inherit_enabled_any` | [`NonInheritEnabledAny`](../../doc/models/non-inherit-enabled-any.md) | Form, Required | - |
| `any_of_additional_properties` | [`AnyOfAdditionalProperties`](../../doc/models/any-of-additional-properties.md) | Form, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AnyOfAdditionalProperties`](../../doc/models/any-of-additional-properties.md).

## Example Usage

```python
non_inherit_enabled_any = NonInheritEnabledAny(
    email='user@example.com',
    additional_properties={
        'stringProperty': jsonpickle.decode('"Some text"'),
        'numberProperty': jsonpickle.decode('123'),
        'booleanProperty': jsonpickle.decode('true'),
        'objectProperty': jsonpickle.decode('{"key":"value"}'),
        'arrayProperty': jsonpickle.decode('[10,20,30]'),
        'parentStringType': jsonpickle.decode('{"name":"Test User","type":"CompSame","company":"OpenAI","additionalProperty1":"Additional Info 1","additionalProperty2":"Additional Info 2"}')
    }
)

any_of_additional_properties = AnyOfAdditionalProperties(
    required_property=ComplexModelWithStringAdditionalProperties(
        name='Complex Model',
        age='35',
        additional_properties={
            'additionalProp': 'string'
        }
    ),
    additional_properties={
        'additionalProperty': ComplexModelWithStringAdditionalProperties(
            name='Additional Property',
            age='30',
            additional_properties={
                'additionalProp1': 'string1'
            }
        )
    }
)

result = form_controller.upload_form_enabled_any(
    non_inherit_enabled_any,
    any_of_additional_properties
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

