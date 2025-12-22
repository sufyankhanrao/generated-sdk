# Pipe Seperated

```python
pipe_seperated_controller = client.pipe_seperated
```

## Class Name

`PipeSeperatedController`

## Methods

* [Get PIPE Seperated in Query](../../doc/controllers/pipe-seperated.md#get-pipe-seperated-in-query)
* [Get Pipe Seperated in Query 1](../../doc/controllers/pipe-seperated.md#get-pipe-seperated-in-query-1)
* [Create Send Pipe Separated Complex Type in Query](../../doc/controllers/pipe-seperated.md#create-send-pipe-separated-complex-type-in-query)
* [Create Send Pipe Separated List of Complex Type in Query](../../doc/controllers/pipe-seperated.md#create-send-pipe-separated-list-of-complex-type-in-query)
* [Create Send Pipe Separated Map of Complex Type in Query](../../doc/controllers/pipe-seperated.md#create-send-pipe-separated-map-of-complex-type-in-query)


# Get PIPE Seperated in Query

```python
def get_pipe_seperated_in_query(self,
                               dependent)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dependent` | `List[int]` | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
dependent = [
    1,
    2,
    3,
    4
]

result = pipe_seperated_controller.get_pipe_seperated_in_query(dependent)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Get Pipe Seperated in Query 1

```python
def get_pipe_seperated_in_query_1(self,
                                 dependent)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `dependent` | `List[str]` | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

## Example Usage

```python
dependent = [
    'ab',
    'bc',
    'cd',
    'ef'
]

result = pipe_seperated_controller.get_pipe_seperated_in_query_1(dependent)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Send Pipe Separated Complex Type in Query

```python
def create_send_pipe_separated_complex_type_in_query(self,
                                                    complex_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complex_type` | [`ComplexType`](../../doc/models/complex-type.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

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

result = pipe_seperated_controller.create_send_pipe_separated_complex_type_in_query(complex_type)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Send Pipe Separated List of Complex Type in Query

```python
def create_send_pipe_separated_list_of_complex_type_in_query(self,
                                                            complex_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complex_type` | [`List[ComplexType]`](../../doc/models/complex-type.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

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

result = pipe_seperated_controller.create_send_pipe_separated_list_of_complex_type_in_query(complex_type)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```


# Create Send Pipe Separated Map of Complex Type in Query

```python
def create_send_pipe_separated_map_of_complex_type_in_query(self,
                                                           complex_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `complex_type` | [`Dict[str, ComplexType]`](../../doc/models/complex-type.md) | Query, Required | - |

## Response Type

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ServerResponse`](../../doc/models/server-response.md).

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

result = pipe_seperated_controller.create_send_pipe_separated_map_of_complex_type_in_query(complex_type)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

