# Unindexed

```python
unindexed_controller = client.unindexed
```

## Class Name

`UnindexedController`

## Methods

* [Create Unindexed Form](../../doc/controllers/unindexed.md#create-unindexed-form)
* [Get Un Indexed Query](../../doc/controllers/unindexed.md#get-un-indexed-query)
* [Create Send String Array in Model - Form](../../doc/controllers/unindexed.md#create-send-string-array-in-model---form)
* [Create Unindexed Body](../../doc/controllers/unindexed.md#create-unindexed-body)
* [Create Send Unindexed Complex Type in Query](../../doc/controllers/unindexed.md#create-send-unindexed-complex-type-in-query)
* [Create Send Unindexed List of Complex Type in Query](../../doc/controllers/unindexed.md#create-send-unindexed-list-of-complex-type-in-query)
* [Create Send Unindexed Map of Complex Type in Query](../../doc/controllers/unindexed.md#create-send-unindexed-map-of-complex-type-in-query)


# Create Unindexed Form

```python
def create_unindexed_form(self,
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

result = un_indexed_controller.create_unindexed_form(model)
print(result)
```


# Get Un Indexed Query

```python
def get_un_indexed_query(self,
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

result = un_indexed_controller.get_un_indexed_query(query_param)
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

result = un_indexed_controller.create_send_string_array_in_model_form(body)
print(result)
```


# Create Unindexed Body

```python
def create_unindexed_body(self,
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

result = un_indexed_controller.create_unindexed_body(model)
print(result)
```


# Create Send Unindexed Complex Type in Query

```python
def create_send_unindexed_complex_type_in_query(self,
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

result = un_indexed_controller.create_send_unindexed_complex_type_in_query(complex_type)
print(result)
```


# Create Send Unindexed List of Complex Type in Query

```python
def create_send_unindexed_list_of_complex_type_in_query(self,
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

result = un_indexed_controller.create_send_unindexed_list_of_complex_type_in_query(complex_type)
print(result)
```


# Create Send Unindexed Map of Complex Type in Query

```python
def create_send_unindexed_map_of_complex_type_in_query(self,
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

result = un_indexed_controller.create_send_unindexed_map_of_complex_type_in_query(complex_type)
print(result)
```

