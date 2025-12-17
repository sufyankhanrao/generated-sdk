# Body

```python
body_controller = client.body
```

## Class Name

`BodyController`

## Methods

* [Upload Simple Model](../../doc/controllers/body.md#upload-simple-model)
* [Upload Date Additional Properties](../../doc/controllers/body.md#upload-date-additional-properties)
* [Upload Date Time Additional Properties](../../doc/controllers/body.md#upload-date-time-additional-properties)
* [Upload UUID Additional Properties](../../doc/controllers/body.md#upload-uuid-additional-properties)
* [Upload Array of String Additional Properties](../../doc/controllers/body.md#upload-array-of-string-additional-properties)
* [Upload Map of Array Additional Properties](../../doc/controllers/body.md#upload-map-of-array-additional-properties)
* [Upload Child Number Type](../../doc/controllers/body.md#upload-child-number-type)
* [Upload Child String Type](../../doc/controllers/body.md#upload-child-string-type)
* [Upload Non Inherit Enabled Number](../../doc/controllers/body.md#upload-non-inherit-enabled-number)
* [Upload Non Inherit Enabled Any](../../doc/controllers/body.md#upload-non-inherit-enabled-any)
* [Upload One of Additional Properties](../../doc/controllers/body.md#upload-one-of-additional-properties)


# Upload Simple Model

Upload SimpleModel

```python
def upload_simple_model(self,
                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SimpleModel`](../../doc/models/simple-model.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SimpleModel`](../../doc/models/simple-model.md).

## Example Usage

```python
body = SimpleModel(
    required_property='Another required property',
    additional_properties={
        'anotherComplexModel': AnotherComplexModel(
            name='Another Complex Model',
            job='Worker',
            additional_properties={
                'salary': '10000 PKR',
                'working Hours': '9 AM to 5 PM'
            }
        ),
        'complexModel': ComplexModel(
            name='Complex Model',
            age='26 Years',
            additional_properties={
                'internalAnotherComplexModel': AnotherComplexModel(
                    name='Internal Another Complex Model',
                    job='Worker',
                    additional_properties={
                        'salary': '10000 PKR',
                        'working Hours': '9 AM to 5 PM'
                    }
                )
            }
        )
    }
)

result = body_controller.upload_simple_model(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Date Additional Properties

```python
def upload_date_additional_properties(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DateAdditionalProperties`](../../doc/models/date-additional-properties.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DateAdditionalProperties`](../../doc/models/date-additional-properties.md).

## Example Usage

```python
body = DateAdditionalProperties(
    required_property=dateutil.parser.parse('2024-11-01').date(),
    additional_properties={
        'additionalProperty1': dateutil.parser.parse('2023-11-01').date(),
        'additionalProperty2': dateutil.parser.parse('2027-11-01').date()
    }
)

result = body_controller.upload_date_additional_properties(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Date Time Additional Properties

```python
def upload_date_time_additional_properties(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DateTimeAdditionalProperties`](../../doc/models/date-time-additional-properties.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DateTimeAdditionalProperties`](../../doc/models/date-time-additional-properties.md).

## Example Usage

```python
body = DateTimeAdditionalProperties(
    required_property=dateutil.parser.parse('2024-11-01T00:00:00Z'),
    additional_properties={
        'additionalProperty1': dateutil.parser.parse('2023-11-01T00:00:00Z'),
        'additionalProperty2': dateutil.parser.parse('2027-11-01T00:00:00Z')
    }
)

result = body_controller.upload_date_time_additional_properties(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload UUID Additional Properties

```python
def upload_uuid_additional_properties(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UUIDAdditionalProperties`](../../doc/models/uuid-additional-properties.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UUIDAdditionalProperties`](../../doc/models/uuid-additional-properties.md).

## Example Usage

```python
body = UUIDAdditionalProperties(
    required_property='123e4567-e89b-12d3-a456-426614174000',
    additional_properties={
        'additionalUUID1': '987e6543-e21b-12d3-a456-426614174000',
        'additionalUUID2': '456e1234-e87b-12d3-a456-426614174000'
    }
)

result = body_controller.upload_uuid_additional_properties(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Array of String Additional Properties

```python
def upload_array_of_string_additional_properties(self,
                                                body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ArrayOfStringAdditionalProperties`](../../doc/models/array-of-string-additional-properties.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ArrayOfStringAdditionalProperties`](../../doc/models/array-of-string-additional-properties.md).

## Example Usage

```python
body = ArrayOfStringAdditionalProperties(
    required_property=[
        'string10',
        'string20'
    ],
    additional_properties={
        'additionalProperty1': [
            'additionalString1',
            'additionalString2'
        ],
        'additionalProperty2': [
            'anotherString1',
            'anotherString2'
        ]
    }
)

result = body_controller.upload_array_of_string_additional_properties(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Map of Array Additional Properties

```python
def upload_map_of_array_additional_properties(self,
                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`MapOfArrayAdditionalProperties`](../../doc/models/map-of-array-additional-properties.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`MapOfArrayAdditionalProperties`](../../doc/models/map-of-array-additional-properties.md).

## Example Usage

```python
body = MapOfArrayAdditionalProperties(
    required_property={
        'key1': 10.1,
        'key2': 20.2
    },
    additional_properties={
        'additionalProperty1': {
            'key1': 3.3,
            'key2': 4.4
        },
        'additionalProperty2': {
            'key1': 5.5
        }
    }
)

result = body_controller.upload_map_of_array_additional_properties(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Child Number Type

```python
def upload_child_number_type(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChildNumberType`](../../doc/models/child-number-type.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChildNumberType`](../../doc/models/child-number-type.md).

## Example Usage

```python
body = ChildNumberType(
    name='Test User',
    company='APIMatic',
    mtype='CompDiff',
    additional_properties={
        'additionalProperty1': 'ParentStringType_additionalProperties3',
        'additionalProperty2': 'ParentStringType_additionalProperties4'
    }
)

result = body_controller.upload_child_number_type(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Child String Type

```python
def upload_child_string_type(self,
                            body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ChildStringType`](../../doc/models/child-string-type.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ChildStringType`](../../doc/models/child-string-type.md).

## Example Usage

```python
body = ChildStringType(
    name='Test User',
    company='OpenAI',
    mtype='CompSame',
    additional_properties={
        'additionalProperty1"': 'Additional Info 1',
        'additionalProperty2"': 'Additional Info 2'
    }
)

result = body_controller.upload_child_string_type(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Non Inherit Enabled Number

```python
def upload_non_inherit_enabled_number(self,
                                     body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NonInheritEnabledNumber`](../../doc/models/non-inherit-enabled-number.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NonInheritEnabledNumber`](../../doc/models/non-inherit-enabled-number.md).

## Example Usage

```python
body = NonInheritEnabledNumber(
    email='test@example.com',
    additional_properties={
        'additionalProperty1': 42.1,
        'additionalProperty2': 100.5
    }
)

result = body_controller.upload_non_inherit_enabled_number(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload Non Inherit Enabled Any

```python
def upload_non_inherit_enabled_any(self,
                                  body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NonInheritEnabledAny`](../../doc/models/non-inherit-enabled-any.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`NonInheritEnabledAny`](../../doc/models/non-inherit-enabled-any.md).

## Example Usage

```python
body = NonInheritEnabledAny(
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

result = body_controller.upload_non_inherit_enabled_any(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Upload One of Additional Properties

```python
def upload_one_of_additional_properties(self,
                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`OneOfAdditionalProperties`](../../doc/models/one-of-additional-properties.md) | Body, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`OneOfAdditionalProperties`](../../doc/models/one-of-additional-properties.md).

## Example Usage

```python
body = OneOfAdditionalProperties(
    required_property=ComplexModelWithStringAdditionalProperties(
        name='Complex Model Name',
        age='30',
        additional_properties={
            'extraDetail': 'Additional detail as per ComplexModel'
        }
    ),
    additional_properties={
        'additionalProperty': ComplexModelWithStringAdditionalProperties(
            name='Additional property Complex Model Name',
            age='300',
            additional_properties={
                'extraDetail': 'Additional property Additional detail as per ComplexModel'
            }
        )
    }
)

result = body_controller.upload_one_of_additional_properties(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

