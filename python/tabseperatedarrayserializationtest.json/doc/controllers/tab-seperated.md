# Tab Seperated

```python
tab_seperated_controller = client.tab_seperated
```

## Class Name

`TabSeperatedController`

## Methods

* [Get Tab Seperated in Query](../../doc/controllers/tab-seperated.md#get-tab-seperated-in-query)
* [Create Send Tab Separated Complex Type in Query](../../doc/controllers/tab-seperated.md#create-send-tab-separated-complex-type-in-query)
* [Create Send Tab Separated List of Complex Type in Query](../../doc/controllers/tab-seperated.md#create-send-tab-separated-list-of-complex-type-in-query)
* [Create Send Tab Separated Map of Complex Type in Query](../../doc/controllers/tab-seperated.md#create-send-tab-separated-map-of-complex-type-in-query)


# Get Tab Seperated in Query

```python
def get_tab_seperated_in_query(self,
                              dependent)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dependent` | `List[str]` | Query, Required | - |

## Response Type

[`ServerResponse`](../../doc/models/server-response.md)

## Example Usage

```python
dependent = [
    'ab',
    'bc',
    'cd',
    'ef'
]

result = tab_seperated_controller.get_tab_seperated_in_query(dependent)
print(result)
```


# Create Send Tab Separated Complex Type in Query

```python
def create_send_tab_separated_complex_type_in_query(self,
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

result = tab_seperated_controller.create_send_tab_separated_complex_type_in_query(complex_type)
print(result)
```


# Create Send Tab Separated List of Complex Type in Query

```python
def create_send_tab_separated_list_of_complex_type_in_query(self,
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

result = tab_seperated_controller.create_send_tab_separated_list_of_complex_type_in_query(complex_type)
print(result)
```


# Create Send Tab Separated Map of Complex Type in Query

```python
def create_send_tab_separated_map_of_complex_type_in_query(self,
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

result = tab_seperated_controller.create_send_tab_separated_map_of_complex_type_in_query(complex_type)
print(result)
```

