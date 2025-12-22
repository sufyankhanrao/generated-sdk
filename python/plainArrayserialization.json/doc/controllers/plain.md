# Plain

```python
plain_controller = client.plain
```

## Class Name

`PlainController`

## Methods

* [Create Plain Form](../../doc/controllers/plain.md#create-plain-form)
* [Get Plain Query](../../doc/controllers/plain.md#get-plain-query)
* [Create Send String Array in Model - Form](../../doc/controllers/plain.md#create-send-string-array-in-model---form)
* [Create Plain Body](../../doc/controllers/plain.md#create-plain-body)
* [Create Send Plain Complex Type in Query](../../doc/controllers/plain.md#create-send-plain-complex-type-in-query)
* [Create Send Plain List of Complex Type in Query](../../doc/controllers/plain.md#create-send-plain-list-of-complex-type-in-query)
* [Create Send Plain Map of Complex Type in Query](../../doc/controllers/plain.md#create-send-plain-map-of-complex-type-in-query)


# Create Plain Form

```python
def create_plain_form(self,
                     model)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Employee`](../../doc/models/employee.md) | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
model = Employee(
    age=15,
    dependents=[
        Person(
            name='rehan',
            field='front-end'
        ),
        Person(
            name='Gill',
            field='back-end'
        )
    ]
)

result = plain_controller.create_plain_form(model)
print(result)
```


# Get Plain Query

```python
def get_plain_query(self,
                   query_param)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `query_param` | `List[str]` | Query, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
query_param = [
    'name',
    'field',
    'address',
    'designation'
]

result = plain_controller.get_plain_query(query_param)
print(result)
```


# Create Send String Array in Model - Form

```python
def create_send_string_array_in_model_form(self,
                                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`Model`](../../doc/models/model.md) | Form, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
body = Model(
    name='farhan',
    dependents=[
        'name',
        'field',
        'address',
        'designation'
    ]
)

result = plain_controller.create_send_string_array_in_model_form(body)
print(result)
```


# Create Plain Body

```python
def create_plain_body(self,
                     model)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `model` | [`Employee`](../../doc/models/employee.md) | Body, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
model = Employee(
    age=15,
    dependents=[
        Person(
            name='rehan',
            field='front-end'
        ),
        Person(
            name='Gill',
            field='back-end'
        )
    ]
)

result = plain_controller.create_plain_body(model)
print(result)
```


# Create Send Plain Complex Type in Query

```python
def create_send_plain_complex_type_in_query(self,
                                           complex_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complex_type` | [`ComplexType`](../../doc/models/complex-type.md) | Query, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
complex_type = ComplexType(
    number_list_type=[
        232
    ],
    number_map_type={
        'key0': 149,
        'key1': 150
    },
    inner_complex_type=InnerComplexType(
        string_type='stringType8',
        boolean_type=False,
        date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        date_type=dateutil.parser.parse('2016-03-13').date(),
        uuid_type='00001742-0000-0000-0000-000000000000',
        long_type=40,
        precision_type=8.18,
        object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
        string_list_type=[
            'stringListType8'
        ]
    ),
    inner_complex_list_type=[
        InnerComplexType(
            string_type='stringType0',
            boolean_type=False,
            date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            date_type=dateutil.parser.parse('2016-03-13').date(),
            uuid_type='00001992-0000-0000-0000-000000000000',
            long_type=88,
            precision_type=70.1,
            object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            string_list_type=[
                'stringListType0',
                'stringListType1',
                'stringListType2'
            ]
        )
    ]
)

result = plain_controller.create_send_plain_complex_type_in_query(complex_type)
print(result)
```


# Create Send Plain List of Complex Type in Query

```python
def create_send_plain_list_of_complex_type_in_query(self,
                                                   complex_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complex_type` | [`List[ComplexType]`](../../doc/models/complex-type.md) | Query, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
complex_type = [
    ComplexType(
        number_list_type=[
            232
        ],
        number_map_type={
            'key0': 149,
            'key1': 150
        },
        inner_complex_type=InnerComplexType(
            string_type='stringType8',
            boolean_type=False,
            date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            date_type=dateutil.parser.parse('2016-03-13').date(),
            uuid_type='00001742-0000-0000-0000-000000000000',
            long_type=40,
            precision_type=8.18,
            object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            string_list_type=[
                'stringListType8'
            ]
        ),
        inner_complex_list_type=[
            InnerComplexType(
                string_type='stringType0',
                boolean_type=False,
                date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                date_type=dateutil.parser.parse('2016-03-13').date(),
                uuid_type='00001992-0000-0000-0000-000000000000',
                long_type=88,
                precision_type=70.1,
                object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                string_list_type=[
                    'stringListType0',
                    'stringListType1',
                    'stringListType2'
                ]
            )
        ]
    )
]

result = plain_controller.create_send_plain_list_of_complex_type_in_query(complex_type)
print(result)
```


# Create Send Plain Map of Complex Type in Query

```python
def create_send_plain_map_of_complex_type_in_query(self,
                                                  complex_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complex_type` | [`Dict[str, ComplexType]`](../../doc/models/complex-type.md) | Query, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
complex_type = {
    'key0': ComplexType(
        number_list_type=[
            232
        ],
        number_map_type={
            'key0': 149,
            'key1': 150
        },
        inner_complex_type=InnerComplexType(
            string_type='stringType8',
            boolean_type=False,
            date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            date_type=dateutil.parser.parse('2016-03-13').date(),
            uuid_type='00001742-0000-0000-0000-000000000000',
            long_type=40,
            precision_type=8.18,
            object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            string_list_type=[
                'stringListType8'
            ]
        ),
        inner_complex_list_type=[
            InnerComplexType(
                string_type='stringType0',
                boolean_type=False,
                date_time_type=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
                date_type=dateutil.parser.parse('2016-03-13').date(),
                uuid_type='00001992-0000-0000-0000-000000000000',
                long_type=88,
                precision_type=70.1,
                object_type=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                string_list_type=[
                    'stringListType0',
                    'stringListType1',
                    'stringListType2'
                ]
            )
        ]
    )
}

result = plain_controller.create_send_plain_map_of_complex_type_in_query(complex_type)
print(result)
```

